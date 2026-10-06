"""Build the Modules 1 and 2 DevNet Associate written reviewer."""

from pathlib import Path
import sys
from html import escape

from docx.shared import Pt
from docx.table import Table as DocxTable
from docx.text.paragraph import Paragraph as DocxParagraph
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "DEVASC M3-M4 Exam Prep"))
from notes_lib import Notes  # noqa: E402


def pdf_from_docx(doc, path):
    """Write a readable PDF from the same document content without Word automation."""
    font_dir = Path("C:/Windows/Fonts")
    for name, filename in (("TNR", "times.ttf"), ("TNR-Bold", "timesbd.ttf"),
                           ("TNR-Italic", "timesi.ttf"), ("TNR-BoldItalic", "timesbi.ttf")):
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-Bold",
                                  italic="TNR-Italic", boldItalic="TNR-BoldItalic")
    styles = {
        "Normal": ParagraphStyle("body", fontName="TNR", fontSize=12, leading=14,
                                 spaceAfter=5),
        "Title": ParagraphStyle("title", fontName="TNR-Bold", fontSize=20, leading=23,
                                alignment=TA_CENTER, spaceAfter=9),
        "Heading 1": ParagraphStyle("h1", fontName="TNR-Bold", fontSize=15, leading=18,
                                    spaceBefore=11, spaceAfter=5, keepWithNext=True),
        "Heading 2": ParagraphStyle("h2", fontName="TNR-Bold", fontSize=13, leading=16,
                                    spaceBefore=8, spaceAfter=4, keepWithNext=True),
        "Heading 3": ParagraphStyle("h3", fontName="TNR-Bold", fontSize=12, leading=15,
                                    spaceBefore=6, spaceAfter=3, keepWithNext=True),
        "List Bullet": ParagraphStyle("bullet", fontName="TNR", fontSize=12,
                                      leading=14, leftIndent=24, firstLineIndent=-12, spaceAfter=2),
        "List Number": ParagraphStyle("number", fontName="TNR", fontSize=12,
                                      leading=14, leftIndent=24, firstLineIndent=-14, spaceAfter=2),
    }
    cell_style = ParagraphStyle("cell", fontName="TNR", fontSize=12, leading=14)
    story = []
    list_number = 0

    def markup(paragraph):
        pieces = []
        for run in paragraph.runs:
            value = escape(run.text).replace("\n", "<br/>")
            if run.bold:
                value = f"<b>{value}</b>"
            if run.italic:
                value = f"<i>{value}</i>"
            pieces.append(value)
        return "".join(pieces)

    for block in doc.iter_inner_content():
        if isinstance(block, DocxParagraph):
            if block._p.xpath('.//w:br[@w:type="page"]'):
                story.append(PageBreak())
                continue
            if not block.text.strip():
                continue
            name = block.style.name
            style = styles.get(name, styles["Normal"])
            prefix = ""
            if name == "List Bullet":
                prefix = "&#8226; "
                list_number = 0
            elif name == "List Number":
                if block._p.xpath('./w:pPr/w:numPr') and (not story or not isinstance(story[-1], Paragraph)
                                                     or story[-1].style.name != "number"):
                    list_number = 0
                list_number += 1
                prefix = f"{list_number}. "
            else:
                list_number = 0
            story.append(Paragraph(prefix + markup(block), style))
        elif isinstance(block, DocxTable):
            data = []
            for row in block.rows:
                data.append([Paragraph("<br/>".join(markup(p) for p in cell.paragraphs), cell_style)
                             for cell in row.cells])
            widths = [cell.width.pt if cell.width else 468 / len(block.columns)
                      for cell in block.rows[0].cells]
            scale = 468 / sum(widths)
            widths = [width * scale for width in widths]
            table = Table(data, colWidths=widths, repeatRows=1 if len(data) > 1 else 0,
                          hAlign="CENTER")
            first_fill = block.rows[0].cells[0]._tc.xpath('./w:tcPr/w:shd')
            fill = first_fill[0].get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fill') if first_fill else None
            commands = [("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BBBBBB")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 5),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                        ("TOPPADDING", (0, 0), (-1, -1), 4),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]
            if fill:
                commands.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#" + fill)))
            table.setStyle(TableStyle(commands))
            story.extend([table, Spacer(1, 5)])

    def footer(canvas, pdf_doc):
        canvas.setFont("TNR", 9)
        canvas.drawRightString(540, 40, str(pdf_doc.page))

    SimpleDocTemplate(str(path), pagesize=(612, 792), leftMargin=72, rightMargin=72,
                      topMargin=72, bottomMargin=72).build(story, onFirstPage=footer,
                                                            onLaterPages=footer)


def main():
    notes = Notes(
        "NetComms 2 Modules 1 and 2 Reviewer",
        "CS0016 Network and Communications 2 | DevNet Associate. "
        "Blue boxes are labeled memory aids for study, not slide text.",
    )
    doc = notes.doc
    normal = doc.styles["Normal"]
    normal.paragraph_format.space_after = Pt(5)
    normal.paragraph_format.line_spacing = 1.15
    for name in ("List Bullet", "List Number", "List Bullet 2"):
        style = doc.styles[name]
        style.font.size = Pt(12)
        style.paragraph_format.space_after = Pt(2)
        style.paragraph_format.line_spacing = 1.1
    for name, before, after in (("Heading 1", 12, 5), ("Heading 2", 9, 4), ("Heading 3", 7, 3)):
        style = doc.styles[name]
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)

    notes.h1("Module 1: Course Introduction")
    notes.p("**Module objective:** Use basic Python programming and Linux skills. The topics prepare you to "
            "install a virtual lab environment, manage the Linux file system and permissions, and use basic Python.")
    notes.h2("Course Overview")
    notes.p("The DevNet Associate course covers software development, networking fundamentals, and automation "
            "through five course modules.")
    notes.table(
        ["Course Module", "What It Covers"],
        [
            ["**Understanding and Using APIs**", "APIs, their benefits, and troubleshooting"],
            ["**Software Development and Design**", "Main software development concepts and tools for quality code"],
            ["**Network Fundamentals**", "Networks, devices, protocols, and connectivity troubleshooting"],
            ["**Infrastructure and Automation**", "Managing infrastructure with automation instead of manual setup"],
            ["**Cisco Platforms and Development**", "Data centers and networking, including data models and security"],
        ], [2.25, 4.25],
    )
    notes.h2("Your Lab Environment")
    notes.p("Virtualization lets virtual computers run within a physical computer. These virtual computers are "
            "**virtual machines (VMs)**. A VM is a **guest**; the physical computer is the **host**. "
            "A modern computer and operating system can run VMs.")
    notes.watch("**Guest = virtual machine. Host = physical computer.** Do not swap the machine running "
                "inside with the machine it runs on.")

    notes.h2("The Three Labs")
    notes.table(
        ["Lab", "Parts"],
        [
            ["**Install the Virtual Lab Environment**", "1. Prepare a computer for virtualization; "
             "2. Explore the DEVASC VM GUI; 3. Create lab environment accounts; "
             "4. Install Webex Teams on your device."],
            ["**Linux Review**", "1. Launch the DEVASC VM; 2. Review command syntax navigation; "
             "3. Review file management; 4. Review regular expressions; 5. Review system administration."],
            ["**Python Programming Review**", "1. Launch the DEVASC VM; 2. Start Python and VS Code; "
             "3. Review data types and variables; 4. Review lists and dictionaries; "
             "5. Review the input function; 6. Review if, for, and while functions; "
             "7. Review methods for file access."],
        ], [2.05, 4.45],
    )
    notes.h2("Linux for DevNet")
    notes.p("Linux is widely used in servers, IoT devices, networking equipment, smartphones, and other devices. "
            "**All coding labs in this course use a Linux-based VM.** If the Linux Review lab is difficult, "
            "**Linux Unhatched** is a free, online, self-paced remedial course.")
    notes.h2("Why Python?")
    notes.numbered([
        "**Easy to learn:** learning takes less time than with many other languages.",
        "**Easy to use:** you can write new software faster.",
        "**Easy to obtain, install, and deploy:** Python is free, open, and multiplatform.",
    ])
    notes.p("Python also provides a foundation for learning other languages, including C++, Java, and C. "
            "If the Python Programming Review lab is difficult, **Python Essentials** on the Student Resources "
            "page is free, online, and self-paced.")
    notes.memory("**M1 readiness chain:** install the VM, review Linux, then review Python. "
                 "Linux Unhatched supports the Linux review; Python Essentials supports the Python review.")

    notes.pagebreak()
    notes.h1("Module 2: The DevNet Developer Environment")
    notes.p("**Module objective:** Implement a development environment using DevNet resources. "
            "Explain how DevNet encourages communities of network programmers and investigate its online resources.")
    notes.h2("What Is DevNet?")
    notes.p("DevNet is a fully integrated developer program with a website, interactive developer community, "
            "coordinated developer tools, integrated discussion forums, and sandboxes.")
    notes.table(
        ["Feature", "Role"],
        [
            ["**Learning Labs**", "Self-paced tutorials, from basic coding to REST APIs with different technologies"],
            ["**Sandboxes**", "Production-like environments for development and testing"],
            ["**Code Exchange**", "Sample code written by other developers"],
            ["**Developer Support**", "Developer issue support through tickets, live chats, and forums"],
            ["**Developer Documentation**", "Central location for product developer API documentation"],
        ], [1.8, 4.7],
    )
    notes.h2("Getting Started with DevNet Resources")
    notes.p("DevNet is a starting point for Cisco APIs, with API documentation, education, and developer support. "
            "The home page at **developer.cisco.com** shows these tiles: Start Now, Learning Tracks, Video Course, "
            "Sandbox, Code Exchange, and Ecosystem Exchange.")
    notes.p("The pictured platform icons are **IoT, Cloud, Networking, Data Center, Security, Mobility, "
            "Open Source, Collaboration, and Services**.")

    notes.h2("DevNet Learning Labs")
    notes.p("Learning Labs provide tutorials on engineering technologies, programming languages, "
            "model-driven programmability, REST APIs, Python, and JavaScript. They also provide a walk-through "
            "for using a DevNet Sandbox already configured with Cisco platforms.")
    notes.p("They enable practice by setting up a development environment on a local computer and offer tutorials "
            "across coding, collaboration, IoT, data center, mobility, and networking topics.")
    notes.pagebreak()
    notes.h2("DevNet Sandbox")
    notes.p("Sandboxes are environments for hands-on exploration of software and APIs. "
            "The slide picture shows these sandbox cards:")
    notes.table(
        ["Sandbox Card", "Detail Shown"],
        [
            ["**Firepower Management Center**", "REST API; reservation only"],
            ["**Meraki Small Business / Meraki Enterprise**", "Meraki sandbox cards"],
            ["**Network Assurance Engine**", "Always-on"],
        ], [3.15, 3.35],
    )
    notes.watch("**Learning Labs = guided tutorials and walk-throughs. Sandbox = the environment "
                "where you explore software and APIs.** A Learning Lab may guide you through a Sandbox.")

    notes.h2("The Three DevNet Exchanges")
    notes.table(
        ["Exchange", "What It Holds"],
        [
            ["**Automation Exchange**", "Network automation use cases with solutions and toolkits: "
             "listing data, adding configurations, and activating policies across domains, users, or devices. "
             "Listings cover tool sets such as Ansible or Puppet and campus or branch, data center, "
             "or service provider infrastructure."],
            ["**Code Exchange**", "Source code and tools. It uses the GitHub API and human moderators "
             "to categorize and display hundreds of related repositories."],
            ["**Ecosystem Exchange**", "More than 1,500 solutions across technologies, industries, "
             "and geographies to start solution design and development."],
        ], [1.65, 4.85],
    )
    notes.watch("**Automation = use cases and toolkits; Code = repositories; Ecosystem = solutions.** "
                "The GitHub API and moderators belong to Code Exchange, not Automation Exchange.")
    notes.memory("**A-C-E:** Automation gives a use case, Code gives source code, Ecosystem gives "
                 "a solution catalog.")

    notes.pagebreak()
    notes.h2("DevNet Developer Support")
    notes.p("Support helps troubleshoot integrations, API connections, and developer use cases on Cisco products. "
            "The three ways to reach it are **log a ticket, post to a community forum, and access a Webex Teams "
            "space**. The slide directs readers to **developer.cisco.com/support**.")
    notes.p("The **Knowledge Base** contains troubleshooting articles. A **Support Case** provides one-on-one "
            "support with a one-business-day response. The **Cisco Developer Community forums** are available "
            "through **devnetsupport.cisco.com**, then Community.")
    notes.table(
        ["Support Option", "Cost", "What The Slide Shows"],
        [
            ["Knowledge Base", "Free", "Troubleshooting articles"],
            ["Community Forum", "Free", "Community discussion"],
            ["Chat with DevNet", "Free", "Chat support"],
            ["Case-Based Ticket", "USD 250 for 1 ticket; USD 950 for 5 tickets", "One-on-one support; "
             "one-business-day response"],
        ], [1.75, 2.05, 2.7],
    )
    notes.h2("Module 2 Summary")
    notes.p("DevNet starts developers with Cisco APIs. Its online resources include Learning Labs, video courses, "
            "Sandbox, Exchanges, and developer support. The **Explore DevNet Resources** lab has two parts: "
            "**find and navigate a Learning Lab**, then **explore more resources**.")

    notes.pagebreak()
    notes.h1("One-Page Cram Sheet")
    notes.table(
        ["Recall Prompt", "Answer"],
        [
            ["M1 objective", "Basic Python and Linux; install VM, manage Linux files and permissions"],
            ["Course modules", "APIs; Software Development and Design; Network Fundamentals; "
             "Infrastructure and Automation; Cisco Platforms and Development"],
            ["Guest / host", "Guest = VM; host = physical computer"],
            ["Three M1 labs", "Install Virtual Lab Environment (4 parts); Linux Review (5); "
             "Python Programming Review (7)"],
            ["Linux", "All coding labs use a Linux-based VM; Linux Unhatched if review is difficult"],
            ["Python", "Easy to learn; fast to write; free, open, multiplatform; foundation for other languages; "
             "Python Essentials if review is difficult"],
            ["M2 objective", "Implement a development environment with DevNet resources"],
            ["Five DevNet features", "Learning Labs; Sandboxes; Code Exchange; Developer Support; "
             "Developer Documentation"],
            ["Labs / Sandbox", "Tutorials and walk-throughs / hands-on testing environment"],
            ["Three Exchanges", "Automation = use cases; Code = GitHub-linked repositories; "
             "Ecosystem = 1,500+ solutions"],
            ["Automation examples", "List data, add configurations, activate policies; Ansible or Puppet; "
             "campus/branch, data center, service provider"],
            ["Support access", "Ticket, community forum, Webex Teams space"],
            ["Support cost", "Knowledge Base, forum, chat: free. Case ticket: USD 250 for 1 or USD 950 for 5; "
             "one business day response"],
        ], [1.7, 4.8],
    )
    notes.memory("**Sort the easy swaps:** guest = VM; Labs = guided learning; Sandbox = practice environment; "
                 "Automation = use cases; Code = repositories; Ecosystem = solutions.")
    output = HERE.parent / "PAMESA - NetComms 2 M1-M2 Reviewer.docx"
    doc.save(output)
    pdf = output.with_suffix(".pdf")
    pdf_from_docx(doc, pdf)
    print(output)
    print(pdf)


if __name__ == "__main__":
    main()
