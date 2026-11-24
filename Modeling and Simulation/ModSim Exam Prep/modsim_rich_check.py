"""Check rich module structure, NoteContent, documents, and the ab5362b deck.

Run after modsim_rich_build.py. Each module's matlab_checks records complete
code and expected_output, mirrored in its visible worked examples. When
D:/bin/matlab.exe exists, replay every snippet in an isolated script workspace
and compare captured output, ignoring only trailing whitespace and outer blanks.
Failures raise an exception and exit nonzero; MATLAB absence is reported, not
misrepresented as successful execution.
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from pypdf import PdfReader

from modsim_rich_build import (HERE, ROOT, OUTPUT, PAYLOAD, TITLE, NoteContent,
                               combined_content, field_span, load_modules)

MATLAB = Path("D:/bin/matlab.exe")
BASELINE = "ab5362b"
SECTION_FIELDS = {"heading", "summary", "key_terms", "properties", "worked_examples",
                  "common_mistakes", "source_refs", "memory_aids", "comparisons"}
CODE = re.compile(r"```matlab\s*\n(.*?)```", re.DOTALL)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def normalized_output(text):
    return "\n".join(line.rstrip() for line in text.replace("\r\n", "\n").splitlines()).strip()


def check_modules(modules):
    totals = {"sections": 0, "comparisons": 0, "memory_aids": 0, "code_examples": 0}
    output_checks = []
    for number, module in enumerate(modules, 1):
        name = f"M{number}"
        raw = (HERE / f"rich_{name}.json").read_text(encoding="utf-8-sig")
        require("\u2014" not in raw, f"{name}: forbidden em dash")
        for field in ("sections", "formula_sheet", "self_check", "cram_sheet"):
            require(field in module, f"{name}: missing {field}")
        NoteContent.model_validate(module)
        require(6 <= len(module["sections"]) <= 10, f"{name}: expected 6 to 10 sections")
        require(4 <= len(module["self_check"]) <= 6, f"{name}: expected 4 to 6 self-checks")
        require(5 <= len(module["cram_sheet"]) <= 8, f"{name}: expected 5 to 8 cram items")
        require(module["formula_sheet"], f"{name}: missing formula sheet")
        checks = module.get("matlab_checks", [])
        require(isinstance(checks, list), f"{name}: matlab_checks must be a list")
        for index, check in enumerate(checks, 1):
            require(set(check) == {"code", "expected_output"},
                    f"{name} MATLAB {index}: expected code and expected_output")
            require(all(isinstance(value, str) and value.strip() for value in check.values()),
                    f"{name} MATLAB {index}: empty code or output")
            output_checks.append((name, index, check))
        counts = {"sections": len(module["sections"]), "comparisons": 0,
                  "memory_aids": 0, "code_examples": 0}
        baseline = json.loads((HERE / f"final_{name}.json").read_text(encoding="utf-8-sig"))
        source_file = baseline["source_file"]
        page_count = len(PdfReader(str(HERE / "sources" / source_file)).pages)
        for section in module["sections"]:
            where = section.get("heading", name)
            require(SECTION_FIELDS <= section.keys(), f"{where}: missing section keys")
            require(section["heading"].startswith(name + ": "), f"{where}: wrong module prefix")
            require(section["summary"].strip(), f"{where}: blank summary")
            require("\n" not in section["summary"], f"{where}: summary must be plain sentences")
            for field in ("key_terms", "properties", "common_mistakes", "source_refs"):
                require(section[field], f"{where}: empty {field}")
            for ref in section["source_refs"]:
                match = re.fullmatch(re.escape(source_file) + r", PDF p\. (\d+(?:, \d+)*)", ref)
                require(match is not None, f"{where}: invalid citation {ref!r}")
                require(all(1 <= int(page) <= page_count for page in match.group(1).split(", ")),
                        f"{where}: citation outside source PDF")
            require("matlab_checks" not in section, f"{where}: put all output checks at module level")
            counts["comparisons"] += len(section["comparisons"])
            counts["memory_aids"] += len(section["memory_aids"])
            for example in section["worked_examples"]:
                snippets = [code.strip() for step in example["steps"] for code in CODE.findall(step)]
                if snippets:
                    counts["code_examples"] += 1
                for snippet in snippets:
                    candidates = [check for check in checks if check["code"].strip() == snippet]
                    require(candidates, f"{where}: worked code has no replay check")
                    require(any(normalized_output(check["expected_output"]) in
                                normalized_output(example["answer"]) for check in candidates),
                            f"{where}: replay output is missing from printed answer")
        for check in checks:
            require(any(check["code"].strip() in step for section in module["sections"]
                        for example in section["worked_examples"] for step in example["steps"]),
                    f"{name}: recorded MATLAB output has no visible code example")
        for key in totals:
            totals[key] += counts[key]
        print(name + ": " + ", ".join(f"{key}={value}" for key, value in counts.items()) +
              f", formulas={len(module['formula_sheet'])}, self_check={len(module['self_check'])}, "
              f"cram={len(module['cram_sheet'])}, matlab_checks={len(checks)}")
    require(totals["comparisons"] >= 25, "Expected at least 25 comparisons")
    require(totals["memory_aids"] >= 20, "Expected at least 20 memory aids")
    require(totals["code_examples"] >= 15, "Expected at least 15 worked examples with MATLAB code")
    return output_checks


def check_payload(modules):
    text = PAYLOAD.read_bytes().decode("utf-8")
    payload = json.loads(text)
    require(len(payload["notes"]) == 1, "Expected exactly one note")
    note = payload["notes"][0]
    require(note["title"] == TITLE, "Wrong note title")
    require("\u2014" not in json.dumps(note, ensure_ascii=False), "Payload note contains an em dash")
    NoteContent.model_validate(note["content"])
    require(note["content"] == combined_content(modules), "Payload note does not match rich modules")
    require(len(payload["decks"]) == 1, "Expected exactly one deck")
    require(len(payload["decks"][0]["cards"]) == 200, "Expected exactly 200 cards")
    result = subprocess.run(["git", "show", f"{BASELINE}:AndyHub Export/payload_modsim_final.json"],
                            cwd=ROOT, capture_output=True, check=True)
    original_text = result.stdout.decode("utf-8")
    original = json.loads(original_text)
    require(payload["decks"][0]["cards"] == original["decks"][0]["cards"],
            "Flashcards differ from the independently reviewed baseline")
    start, end = field_span(text, "decks")
    old_start, old_end = field_span(original_text, "decks")
    # Git checkout uses CRLF here; ignore only that checkout conversion.
    require(text[start:end].replace("\r\n", "\n").encode("utf-8") ==
            original_text[old_start:old_end].replace("\r\n", "\n").encode("utf-8"),
            "Deck serialization differs from baseline beyond checkout line endings")
    require("\u2014" not in (HERE / "modsim_rich_build.py").read_text(encoding="utf-8"),
            "Build script contains an em dash")
    print("Payload: schema valid; rich content matches; all 200 baseline cards and deck serialization unchanged.")


def check_documents(modules):
    doc = Document(str(OUTPUT.with_suffix(".docx")))
    require(doc.styles["Normal"].font.name == "Times New Roman", "Wrong DOCX body font")
    require(doc.styles["Normal"].font.size.pt == 12, "Wrong DOCX body font size")
    word_text = "\n".join(p.text for p in doc.paragraphs)
    pdf = PdfReader(str(OUTPUT.with_suffix(".pdf")))
    pages = [page.extract_text() or "" for page in pdf.pages]
    require(pages and all(page.strip() for page in pages), "PDF has an empty or unreadable page")
    pdf_text = " ".join(" ".join(pages).split())
    for module in modules:
        for section in module["sections"]:
            require(section["heading"] in word_text, f"DOCX missing {section['heading']}")
            require(" ".join(section["heading"].split()) in pdf_text,
                    f"PDF missing {section['heading']}")
    print(f"Documents: DOCX Times New Roman 12; PDF {len(pages)} readable pages with every module section.")


def run_matlab(checks):
    if not MATLAB.is_file():
        print(f"MATLAB: SKIPPED ({MATLAB} not installed); recorded outputs were not executed on this machine.")
        return
    require(checks, "No MATLAB outputs recorded")
    quote = lambda value: str(value).replace("'", "''")
    with tempfile.TemporaryDirectory(prefix="rich_matlab_", dir=HERE) as directory:
        folder = Path(directory)
        commands = []
        for index, (_, _, check) in enumerate(checks, 1):
            script = folder / f"example_{index:03}.m"
            script.write_text(check["code"] + "\n", encoding="utf-8")
            output = folder / f"output_{index:03}.txt"
            commands.append(
                f"actual = capture_output('{quote(script.as_posix())}');\n"
                f"fid = fopen('{quote(output.as_posix())}', 'w', 'n', 'UTF-8');\n"
                "assert(fid >= 0, 'Cannot write captured output');\n"
                "fprintf(fid, '%s', actual); fclose(fid);")
        commands.append("disp('ALL_RICH_MATLAB_EXAMPLES_EXECUTED');\n"
                        "function captured = capture_output(script_path)\n"
                        "captured = evalc('run(script_path)');\nend")
        runner = folder / "rich_output_checks.m"
        runner.write_text("\n".join(commands) + "\n", encoding="utf-8")
        result = subprocess.run([str(MATLAB), "-batch", f"run('{quote(runner.as_posix())}')"],
                                cwd=HERE, capture_output=True, text=True, timeout=900)
        require(result.returncode == 0,
                f"MATLAB execution failed:\n{result.stdout}\n{result.stderr}")
        require("ALL_RICH_MATLAB_EXAMPLES_EXECUTED" in result.stdout,
                "MATLAB did not execute all snippets")
        failures = []
        for index, (module, local_index, check) in enumerate(checks, 1):
            actual = (folder / f"output_{index:03}.txt").read_text(encoding="utf-8-sig")
            if normalized_output(actual) != normalized_output(check["expected_output"]):
                failures.append(f"{module} MATLAB {local_index}: expected {check['expected_output']!r}; got {actual!r}")
            else:
                print(f"MATLAB {module}/{local_index}: {normalized_output(actual)!r}")
        require(not failures, "MATLAB output mismatch:\n" + "\n".join(failures))
    print(f"MATLAB: all {len(checks)} recorded snippets executed; printed outputs matched.")


def main():
    modules = load_modules()
    checks = check_modules(modules)
    check_payload(modules)
    check_documents(modules)
    run_matlab(checks)
    print("PASS: ModSim rich reviewer acceptance check.")


if __name__ == "__main__":
    main()
