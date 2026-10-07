"""Export the remaining midterm reviewers and verified exam decks for AndyHub."""
import json
from pathlib import Path

from export_statana_mobprog import ROOT, OUT, Rec, card, clean, load, note, record, table_cards

SE = ROOT / "Software Engineering 1" / "SE1 Exam Prep"
NC12 = ROOT / "Network and Communications 2" / "DEVASC M1-M2 Exam Prep"
NC34 = ROOT / "Network and Communications 2" / "DEVASC M3-M4 Exam Prep"
MOD = ROOT / "Modeling and Simulation" / "ModSim Exam Prep"


def capture_build(module, method, skip_pdf):
    """Record builder calls while suppressing its document and PDF output."""
    captured = []

    class Capture(Rec):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            captured.append(self)
            self.doc.save = lambda path: None

    original_notes = module.Notes
    original_pdf = getattr(module, skip_pdf)
    module.Notes = Capture
    setattr(module, skip_pdf, lambda *args: None)
    try:
        getattr(module, method)()
    finally:
        module.Notes = original_notes
        setattr(module, skip_pdf, original_pdf)
    return captured[0].ops


def split_modules(ops, prefix, count):
    parts = {number: [] for number in range(1, count + 1)}
    current = None
    for op in ops:
        if op[0] == "h1":
            current = next((number for number in parts if op[1].startswith(f"{prefix} {number}")), None)
        if current:
            parts[current].append(op)
    return parts


EXTRA = {
    ("SE1", 1): [
        ("Which software category operates and controls computer hardware?", "System software", ["Application software", "Embedded software", "Web applications"]),
        ("Which software engineering layer is the bedrock?", "Quality focus", ["Tools", "Methods", "Process"]),
        ("Which process framework activity gathers stakeholder needs?", "Communication", ["Construction", "Deployment", "Modeling"]),
        ("Which process framework activity delivers the product to users?", "Deployment", ["Communication", "Planning", "Modeling"]),
        ("Which information system records daily transactions?", "Transaction Processing System", ["Decision Support System", "Executive Information System", "Expert System"]),
        ("Which information system helps managers decide without making the decision for them?", "Decision Support System", ["Transaction Processing System", "Workflow System", "ERP"]),
        ("Which SDLC phase follows planning?", "Analysis", ["Design", "Testing", "Maintenance"]),
        ("Which SDLC phase tests the built system?", "Testing", ["Planning", "Analysis", "Maintenance"]),
        ("Which SDLC phase keeps the deployed system useful over time?", "Maintenance", ["Planning", "Design", "Testing"]),
        ("Which system has predictable behavior without outside input?", "Closed system", ["Open system", "Probabilistic system", "Notional system"]),
        ("Which information-system activity returns results to adjust input or processing?", "Feedback", ["Input", "Output", "Storage"]),
    ],
    ("SE1", 2): [
        ("Who is associated with the chart used for project scheduling?", "Henry Gantt", ["Henri Fayol", "Frederick Taylor", "Winston Royce"]),
        ("Which chart places project tasks against time?", "Gantt chart", ["Pareto chart", "Control chart", "Histogram"]),
        ("What does a PERT critical path determine?", "The longest path through project activities", ["The cheapest activity", "The shortest task", "The most staffed team"]),
        ("What is the critical-path length in the reviewer's PERT example?", "7 months", ["5 months", "6 months", "8 months"]),
        ("Which project-management phase starts the project?", "Initiation", ["Execution", "Closing", "Monitoring and Controlling"]),
        ("Which project-management phase formally ends the project?", "Closing", ["Initiation", "Execution", "Planning and Design"]),
        ("Which project-management area handles project uncertainties?", "Risk management", ["Scope management", "Cost management", "Procurement management"]),
        ("Which activity breaks a whole into its component parts?", "Analysis", ["Synthesis", "Deployment", "Implementation"]),
        ("Which activity combines parts into a whole?", "Synthesis", ["Analysis", "Decomposition", "Scope definition"]),
        ("Which analysis procedure determines what lies within the project?", "Scope definition", ["Logical design", "Decision analysis", "Problem analysis"]),
        ("Which project characteristic means its details become clearer over time?", "Progressively elaborated", ["Permanent", "Routine", "Unbounded"]),
    ],
    ("DevNet", 1): [
        ("In the virtual lab, what is the guest?", "The virtual machine", ["The physical computer", "The router", "The browser"]),
        ("In the virtual lab, what is the host?", "The physical computer", ["The virtual machine", "The Linux shell", "The Python interpreter"]),
        ("Which operating system is used for the coding labs?", "Linux", ["Windows only", "macOS only", "Android"]),
        ("Which language does the introductory programming review use?", "Python", ["Java", "Go", "C++"]),
        ("Which M1 lab covers file-system navigation and permissions?", "Linux Review", ["Python Programming Review", "Install Virtual Lab Environment", "DevNet Sandbox"]),
        ("Which M1 lab sets up the virtual environment?", "Install Virtual Lab Environment", ["Linux Review", "Python Programming Review", "Code Exchange"]),
        ("How many parts are in the M1 Python Programming Review lab?", "7", ["4", "5", "2"]),
        ("How many parts are in the M1 Linux Review lab?", "5", ["4", "7", "2"]),
        ("Which course module covers APIs and their benefits?", "Understanding and Using APIs", ["Network Fundamentals", "Infrastructure and Automation", "Cisco Platforms and Development"]),
        ("Which course module covers networking devices and protocols?", "Network Fundamentals", ["Understanding and Using APIs", "Software Development and Design", "Cisco Platforms and Development"]),
        ("Which course module emphasizes automated infrastructure management?", "Infrastructure and Automation", ["Network Fundamentals", "Understanding and Using APIs", "Software Development and Design"]),
        ("Which M1 lab reviews regular expressions?", "Linux Review", ["Python Programming Review", "Install Virtual Lab Environment", "Explore DevNet Resources"]),
        ("Which M1 lab reviews lists and dictionaries?", "Python Programming Review", ["Linux Review", "Install Virtual Lab Environment", "Explore DevNet Resources"]),
        ("Which M1 lab reviews file access methods?", "Python Programming Review", ["Linux Review", "Install Virtual Lab Environment", "Explore DevNet Resources"]),
        ("Which M1 lab includes installing Webex Teams?", "Install Virtual Lab Environment", ["Linux Review", "Python Programming Review", "Explore DevNet Resources"]),
        ("Which course is suggested when the Linux Review is difficult?", "Linux Unhatched", ["Python Essentials", "Learning Labs", "Code Exchange"]),
        ("Which course is suggested when the Python Review is difficult?", "Python Essentials", ["Linux Unhatched", "Network Fundamentals", "Developer Documentation"]),
        ("What runs virtual computers inside a physical computer?", "Virtualization", ["Packet routing", "Code Exchange", "Compilation"]),
        ("How many parts are in the Install Virtual Lab Environment lab?", "4", ["5", "7", "2"]),
        ("Which M1 lab launches the DEVASC VM and reviews system administration?", "Linux Review", ["Python Programming Review", "Install Virtual Lab Environment", "Explore DevNet Resources"]),
    ],
    ("DevNet", 2): [
        ("Which DevNet resource offers guided tutorials and walk-throughs?", "Learning Labs", ["Sandboxes", "Code Exchange", "Developer Support"]),
        ("Which DevNet resource gives a hands-on testing environment?", "Sandboxes", ["Learning Labs", "Developer Documentation", "Ecosystem Exchange"]),
        ("Which exchange links to GitHub repositories?", "Code Exchange", ["Automation Exchange", "Ecosystem Exchange", "Learning Labs"]),
        ("Which exchange presents automation use cases?", "Automation Exchange", ["Code Exchange", "Ecosystem Exchange", "Developer Support"]),
        ("Which exchange lists over 1,500 solutions?", "Ecosystem Exchange", ["Code Exchange", "Automation Exchange", "Learning Labs"]),
        ("Which DevNet resource describes APIs and platforms?", "Developer Documentation", ["Sandboxes", "Code Exchange", "Automation Exchange"]),
        ("Which DevNet support route is a paid case?", "Case ticket", ["Knowledge Base", "Community forum", "Chat"]),
        ("Which tools are named as automation examples?", "Ansible and Puppet", ["Excel and Word", "MATLAB and Simulink", "Docker and Kubernetes"]),
        ("Which Sandbox card is marked always-on in the reviewer?", "Network Assurance Engine", ["Firepower Management Center", "Meraki Enterprise", "Meraki Small Business"]),
        ("Which Sandbox card is reservation-only in the reviewer?", "Firepower Management Center", ["Network Assurance Engine", "Meraki Enterprise", "Meraki Small Business"]),
        ("Which DevNet resource has a central product API documentation location?", "Developer Documentation", ["Learning Labs", "Sandboxes", "Code Exchange"]),
        ("Which technology links and categorizes repositories in Code Exchange?", "GitHub API", ["MATLAB API", "Webex API", "Canvas API"]),
    ],
    ("ModSim", 1): [
        ("What is a model?", "A representation of a system", ["The actual system", "An observation only", "A random number"]),
        ("What does simulation do?", "Operates or imitates a system through a model", ["Only draws a system", "Eliminates model validation", "Replaces all analysis"]),
        ("Which system type changes state at distinct instants?", "Discrete", ["Continuous", "Static", "Closed"]),
        ("Which system type changes state smoothly over time?", "Continuous", ["Discrete", "Static", "Notional"]),
        ("What is an entity's property called?", "Attribute", ["Activity", "Boundary", "Event"]),
        ("What is the collection of relevant values at one time?", "State", ["Scale", "Resolution", "Fidelity"]),
        ("Which activity originates outside the system boundary?", "Exogenous", ["Endogenous", "Deterministic", "Continuous"]),
        ("Which activity has fully input-determined output?", "Deterministic", ["Stochastic", "Exogenous", "Notional"]),
        ("Which model check compares behavior with its intended real-world purpose?", "Validation", ["Verification", "Compilation", "Visualization"]),
        ("Which simulation type jumps between state-changing events?", "Discrete-event simulation", ["Continuous simulation", "Static modeling", "Analytical solution"]),
        ("What does model fidelity describe?", "Realism", ["Scenario size", "Level of detail", "Execution speed"]),
    ],
    ("ModSim", 2): [
        ("What does a cumulative distribution function F(x) give?", "P(X ≤ x)", ["P(X = x) only", "The sample mean", "The variance"]),
        ("What is the total area under a continuous probability density?", "1", ["0", "0.5", "2"]),
        ("Which distribution is specified by lower bound, upper bound, and mode?", "Triangular", ["Uniform", "Exponential", "Normal"]),
        ("Which distribution models interarrival time using its mean?", "Exponential", ["Normal", "Uniform", "Triangular"]),
        ("Which queue discipline serves arrivals in order?", "FIFO", ["LIFO", "Random", "Priority only"]),
        ("Which queue discipline serves the newest arrival first?", "LIFO", ["FIFO", "Round robin", "Shortest job first"]),
        ("For one customer, how is service beginning time computed?", "max(arrival time, previous end time)", ["min(arrival time, previous end time)", "arrival time plus service time", "previous end time minus arrival time"]),
        ("How is a customer's waiting time computed?", "Service beginning time minus arrival time", ["End time minus beginning time", "Arrival time plus service time", "Idle time plus end time"]),
        ("What does a next-event simulation clock advance to?", "The earliest scheduled event", ["The next fixed second", "The final customer", "The largest random value"]),
        ("What is the total waiting time in the six-customer example?", "4 minutes", ["3 minutes", "7 minutes", "19 minutes"]),
        ("What is the total time in system in the six-customer example?", "19 minutes", ["4 minutes", "3 minutes", "10 minutes"]),
        ("How many events are in the full power set of k outcomes?", "2^k", ["k", "k^2", "2k"]),
        ("What is the probability of the whole sample space?", "1", ["0", "0.5", "2"]),
        ("What is the inverse of f(x)=mx+b when m is nonzero?", "(y-b)/m", ["my+b", "m/(y-b)", "y/(m+b)"]),
        ("Which distribution is specified by a mean and standard deviation?", "Normal", ["Uniform", "Triangular", "Exponential"]),
        ("Which input model draws only previously observed values?", "Direct sample", ["Theoretical distribution", "Differential equation", "Random seed"]),
        ("What orders scheduled events in a discrete-event simulation?", "Future event list", ["Output report", "Resource pool", "Input sample"]),
        ("What is resource utilization?", "Busy time divided by observed time", ["Idle time divided by busy time", "Waiting time divided by service time", "Arrivals divided by departures"]),
        ("What does a customer do by leaving a queue after joining it?", "Renege", ["Balk", "Jockey", "Faff"]),
        ("What does a customer do by declining to join a queue?", "Balk", ["Renege", "Jockey", "Faff"]),
        ("What does a customer do by switching queues?", "Jockey", ["Balk", "Renege", "Faff"]),
        ("How many baristas minimize total cost in the coffee-shop example?", "2", ["1", "3", "4"]),
    ],
    ("ModSim", 3): [
        ("What do continuous-system state equations determine?", "State derivatives", ["Chart colors", "Random seeds", "Queue discipline"]),
        ("What do output equations calculate?", "Requested measurements", ["State derivatives only", "Random seeds", "Simulation clock jumps"]),
        ("Which MATLAB operator multiplies arrays element by element?", ".*", ["*", ".^", "./"]),
        ("Which MATLAB operator raises array elements to a power?", ".^", ["^", ".*", "./"]),
        ("What is the first MATLAB array index?", "1", ["0", "-1", "2"]),
        ("What does MATLAB's mod(x,2)==0 identify for an integer x?", "Even number", ["Odd number", "Negative number", "Prime number"]),
        ("What does MATLAB's percent sign start?", "A comment", ["A modulo expression", "A string", "A loop"]),
        ("Which MATLAB command opens a new plot window?", "figure", ["subplot", "legend", "grid on"]),
        ("Which MATLAB command creates a grid of axes in one figure?", "subplot", ["figure", "axis equal", "xlabel"]),
        ("What does plot(x,y,'r*') display?", "Red star markers", ["A red solid line only", "Blue stars", "A bar chart"]),
        ("What does input(...,'s') read?", "Text", ["A numeric matrix only", "A figure", "A file path only"]),
        ("What does a MATLAB function use for its variables?", "Local scope", ["Only the base workspace", "Global scope by default", "No variables"]),
        ("Which numerical method uses the current tangent slope for one step?", "Forward Euler", ["Midpoint RK2", "Next-event advance", "Monte Carlo sampling"]),
        ("Which numerical method uses a slope evaluated halfway through the step?", "Midpoint RK2", ["Forward Euler", "Next-event advance", "Fixed-increment advance"]),
        ("Which Lotka-Volterra variable denotes prey in the reviewer?", "x", ["y", "b", "d"]),
        ("Which Lotka-Volterra variable denotes predators in the reviewer?", "y", ["x", "b", "p"]),
        ("Which MATLAB command displays a value without its variable name?", "disp", ["fprintf", "fscanf", "input"]),
        ("Which MATLAB command selects equal unit scales on the axes?", "axis equal", ["axis square", "hold on", "grid on"]),
        ("Which MATLAB command creates a square plotting box?", "axis square", ["axis equal", "hold on", "grid on"]),
        ("What does a MATLAB script use for its variables?", "The workspace", ["Only local function scope", "Only global declarations", "No variables"]),
        ("Which MATLAB loop repeats while a condition remains true?", "while", ["for", "switch", "if"]),
    ],
}


def old_cards(path, title):
    rows = json.loads(path.read_text(encoding="utf-8"))[title]["cards"]
    result = []
    for row in rows:
        if row[2] != "multiple_choice":
            continue
        options = json.loads(row[5])
        if len(options) == 4 and len(set(options)) == 4 and row[4] in options:
            result.append({"type": "multiple_choice", "question": row[3],
                           "correct_answer": row[4], "options": row[5], "times_missed": 0})
    return result


def module_cards(kind, number, ops):
    cards = [card(*item) for item in EXTRA[(kind, number)]]
    seen = {item["question"] for item in cards}
    for candidate in table_cards(ops):
        if candidate["question"] not in seen and len(cards) < 40:
            cards.append(candidate)
            seen.add(candidate["question"])
    return cards


def deck(name, subject, groups):
    cards = []
    for index in range(max(map(len, groups))):
        cards.extend(group[index] for group in groups if index < len(group))
    if len({item["question"] for item in cards}) != len(cards):
        raise ValueError(f"Duplicate questions in {name}")
    return {"name": name, "modules_included": ", ".join(f"M{n}" for n in range(1, len(groups) + 1)),
            "subject": subject, "module_ids": None, "cards": cards}


def main():
    se = load("se1_m1m2_export", SE / "se1_m1m2_notes.py")
    nc = load("netcomms_m1m2_export", NC12 / "netcomms_m1m2_notes.py")
    mod = load("modsim_export", MOD / "modsim_notes.py")
    ops = {("SE1", n): record(getattr(se, f"m{n}")) for n in (1, 2)}
    ops.update({("DevNet", n): part for n, part in split_modules(
        capture_build(nc, "main", "pdf_from_docx"), "Module", 2).items()})
    ops.update({("ModSim", n): part for n, part in split_modules(
        capture_build(mod, "build", "save_pdf"), "Module", 3).items()})
    subjects = {"SE1": "Software Engineering 1", "DevNet": "Network and Communications 2",
                "ModSim": "Modeling and Simulation"}
    notes = []
    for kind, count in (("SE1", 2), ("DevNet", 2), ("ModSim", 3)):
        for n in range(1, count + 1):
            if kind == "SE1":
                refs = [p.name for p in sorted((SE / "sources_m1m2").iterdir())
                        if p.name.startswith("CS0024-M1" if n == 1 else "CS0025-M2")]
                refs.append("image_slides_notes.md")
            elif kind == "DevNet":
                refs = [f"DEVASC_Module_{n}.txt"]
            else:
                refs = [p.name for p in sorted((MOD / "sources").iterdir()) if p.name.startswith(f"M{n}-")]
                refs.append("image_slides_notes.md")
            notes.append(note(f"{kind} Module {n} Reviewer Notes", subjects[kind], ops[(kind, n)], refs))
    se_old = SE / "andyhub_se1_decks.json"
    nc_old = NC34 / "andyhub_decks.json"
    decks = [
        deck("SE1_M1-M4_Midterm_Verified", subjects["SE1"],
             [module_cards("SE1", n, ops[("SE1", n)]) for n in (1, 2)] +
             [old_cards(se_old, title) for title in (
                 "SE1 Module 3 Agile Methodologies", "SE1 Module 4 System Models and Requirements")]),
        deck("DevNet_M1-M4_Midterm_Verified", subjects["DevNet"],
             [module_cards("DevNet", n, ops[("DevNet", n)]) for n in (1, 2)] +
             [old_cards(nc_old, title) for title in (
                 "DEVASC Module 3 Software Development and Design", "DEVASC Module 4 Understanding and Using APIs")]),
        deck("ModSim_M1-M3_Midterm_Verified", subjects["ModSim"],
             [module_cards("ModSim", n, ops[("ModSim", n)]) for n in (1, 2, 3)]),
    ]
    (OUT / "notes_se1_netcomms_modsim.json").write_text(json.dumps(notes, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / "decks_se1_netcomms_modsim.json").write_text(json.dumps(decks, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Exported {len(notes)} notes and {len(decks)} decks: {[len(d['cards']) for d in decks]} cards")


if __name__ == "__main__":
    main()
