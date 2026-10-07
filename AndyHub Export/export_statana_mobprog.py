"""Export the CS0073 and CS0011 reviewers and verified exam decks for AndyHub."""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
STAT = ROOT / "Statistical Analysis and Modeling" / "StatAna Exam Prep"
MOB = ROOT / "Mobile Programming" / "MobProg Exam Prep"
SE = ROOT / "Software Engineering 1" / "SE1 Exam Prep"
NC = ROOT / "Network and Communications 2" / "DEVASC M3-M4 Exam Prep"
HUB = Path(r"D:\Personal Projects\All In One Reviewer")
for path in (SE, NC, HUB, STAT, MOB):
    sys.path.insert(0, str(path))

from notes_to_andyhub import Rec, clean
from notes_to_andyhub_v2 import convert_v2
from andyhub_api.schemas import NoteContent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def record(fn):
    rec = Rec("Reviewer", "Slide-based notes")
    fn(rec)
    return rec.ops


def split_m1m2(module):
    original = module.Notes
    module.Notes = Rec
    try:
        # build() creates its own Notes object; Rec.save() discards the DOCX.
        captured = []
        class Capture(Rec):
            def save(self, path):
                captured.extend(self.ops)
        module.Notes = Capture
        module.build()
    finally:
        module.Notes = original
    parts = {1: [], 2: []}
    current = None
    for op in captured:
        if op[0] == "h1" and op[1].startswith("Part 1:"):
            current = 1
        elif op[0] == "h1" and op[1].startswith("Part 2:"):
            current = 2
        elif op[0] == "h1" and "Cram Sheet" in op[1]:
            current = None
        if current:
            parts[current].append(op)
    return parts


def note(title, subject, ops, refs):
    sections, cram = convert_v2(ops, refs)
    content = NoteContent.model_validate({"sections": sections, "formula_sheet": [],
                                          "self_check": [], "cram_sheet": cram})
    return {"title": title, "subject": subject, "module_ids": [],
            "content": content.model_dump(mode="json")}


def card(question, answer, other):
    options = [answer, *other]
    assert len(options) == 4 and len(set(options)) == 4
    return {"type": "multiple_choice", "question": question,
            "correct_answer": answer, "options": json.dumps(options, ensure_ascii=False),
            "times_missed": 0}


def table_cards(ops):
    """Turn unambiguous slide table rows into recognition questions."""
    groups = []
    heading = "Module"
    for op in ops:
        if op[0] in ("h1", "h2"):
            heading = clean(op[1])
        if op[0] != "table":
            continue
        headers, rows = op[1:3]
        if len(rows) < 4:
            continue
        labels = [clean(r[0]) for r in rows]
        if len(set(labels)) != len(labels):
            continue
        group = []
        for col in range(1, len(headers)):
            values = [clean(r[col]) for r in rows]
            if any(not v for v in values) or len(set(values)) != len(values):
                continue
            for i, label in enumerate(labels):
                others = [values[(i + step) % len(values)] for step in (1, 2, 3)]
                group.append(card(f"In {heading}, which {clean(headers[col]).lower()} matches {label}?",
                                  values[i], others))
                # Reverse matching gives a different recognition task with short options.
                label_options = [labels[(i + step) % len(labels)] for step in (1, 2, 3)]
                group.append(card(f"In {heading}, which {clean(headers[0]).lower()} matches: {values[i]}?",
                                  label, label_options))
        if group:
            groups.append(group)
    result = []
    for i in range(max(map(len, groups), default=0)):
        result.extend(group[i] for group in groups if i < len(group))
    return result


# Explicit corrections and the sparsely tabulated diagnostic module. These are
# facts from the reviewer builders and their slide transcriptions, not generated text.
EXTRA = {
    ("StatAna", 1): [
        ("Which Excel function averages values meeting one criterion?", "AVERAGEIF", ["AVERAGE", "AVERAGEIFS", "SUMIF"]),
        ("Which Excel function counts cells containing numbers?", "COUNT", ["COUNTA", "COUNTBLANK", "COUNTIF"]),
        ("Which Excel function counts nonblank cells?", "COUNTA", ["COUNT", "COUNTBLANK", "COUNTIF"]),
        ("Which Excel function calculates sample standard deviation?", "STDEV", ["STDEVP", "VAR", "VARP"]),
        ("Which kind of variation is shown by a point outside the control limits?", "Special cause", ["Common cause", "Central tendency", "Sampling variation"]),
    ],
    ("StatAna", 2): [
        ("What question does diagnostic analytics answer?", "Why did it happen?", ["What happened?", "What will happen?", "What should we do?"]),
        ("What does diagnostic analytics investigate in historical data?", "Underlying drivers", ["Future forecasts", "Optimal actions", "App layouts"]),
        ("Which diagnostic function notices unusual results?", "Identify anomalies", ["Predict outcomes", "Optimize resources", "Present totals"]),
        ("Which diagnostic function investigates details to find an explanation?", "Drill into analytics", ["Forecast outcomes", "Aggregate totals", "Recommend actions"]),
        ("Which diagnostic function examines possible causes?", "Determine causal relationships", ["Determine casual relationships", "Calculate quartiles", "Select a forecast"]),
        ("Which method does the slide map to factors that move together?", "Correlation coefficient", ["Chi-Square", "ANOVA F-test", "Z-test"]),
        ("Which method does the slide map to different categorical distributions?", "Chi-Square", ["Correlation coefficient", "Moving average", "Linear regression"]),
        ("Which method does the slide map to similar populations?", "ANOVA (F-test)", ["Correlation coefficient", "Chi-Square", "Pareto chart"]),
        ("Which tests does the slide place under analysis of means?", "Z-test and T-test", ["Chi-Square and correlation", "Pareto and SPC", "Median and mode"]),
        ("What kind of relationship can association include?", "A curved relationship", ["Only a linear relationship", "Only a positive relationship", "Only a negative relationship"]),
        ("What kind of relationship does correlation measure?", "A linear relationship", ["Any curved relationship", "Only a causal relationship", "Only a categorical relationship"]),
        ("Can a U-shaped pattern be associated without linear correlation?", "Yes", ["No", "Only with a positive slope", "Only with a negative slope"]),
        ("Which is a possible direction of linear correlation?", "Negative", ["Causal", "Categorical", "Prescriptive"]),
        ("Which analytics type identifies data anomalies?", "Diagnostic", ["Descriptive", "Predictive", "Prescriptive"]),
        ("Which analytics type reconfigures data into an easily read format?", "Descriptive", ["Diagnostic", "Predictive", "Prescriptive"]),
        ("Which analytics type highlights trends and relationships to investigate causes?", "Diagnostic", ["Descriptive", "Predictive", "Prescriptive"]),
        ("Which analytics type describes current performance or outcome?", "Descriptive", ["Diagnostic", "Predictive", "Prescriptive"]),
        ("Which analytics type answers what happened?", "Descriptive", ["Diagnostic", "Predictive", "Prescriptive"]),
        ("Which analytics type answers why it happened?", "Diagnostic", ["Descriptive", "Predictive", "Prescriptive"]),
        ("What data period do both descriptive and diagnostic analytics use in the slide comparison?", "Historical data", ["Only future data", "Only simulated data", "Only real-time data"]),
        ("Which named method assesses factors moving together?", "Correlation coefficient", ["T-test", "ANOVA", "Chi-Square"]),
        ("Which named method is associated with an F-test?", "ANOVA", ["Correlation", "Chi-Square", "Moving average"]),
        ("Which named test is listed in the module objectives without a worked example?", "One-way ANOVA", ["Multiple regression", "MAPE", "SPC"]),
        ("Which statement about association is correct?", "It need not be linear", ["It is always linear", "It proves causation", "It is always positive"]),
        ("Which statement corrects the slide's 'casual relationships' typo?", "Causal relationships", ["Casual relationships", "Correlational predictions", "Categorical forecasts"]),
    ],
    ("StatAna", 3): [
        ("At the 0.05 level, which ad-spend predictor is insignificant in the regression table?", "Newspaper", ["TV", "Radio", "Intercept"]),
        ("What is the regression table's R Square?", "0.893710", ["0.891366", "0.94536", "1.736514"]),
        ("What fitted model is printed on the p28 slide?", "Sales = 2.98 + 0.047 x TV + 0.178 x Radio", ["Sales = 3.045 + 0.047 x TV + 0.180 x Radio", "Sales = 2.98 + 0.178 x TV + 0.047 x Radio", "Sales = 2.98 + 0.047 x TV - 0.178 x Radio"]),
        ("Which forecast measure divides absolute error by actual Y?", "MAPE", ["MAE", "MSE", "RMSE"]),
    ],
    ("MobProg", 1): [
        ("Which runtime appears in the supplied Android architecture diagram?", "Dalvik", ["ART only", "JVM only", "Node.js"]),
        ("Which runtime does the Lollipop version slide name?", "ART", ["Dalvik", "JVM", "V8"]),
    ],
    ("MobProg", 2): [
        ("Which project template do the written M2 steps name?", "Empty Activity", ["Empty Views Activity", "Basic Views Activity", "No Activity"]),
        ("Which template is selected in the M2 screenshot?", "Empty Views Activity", ["Empty Activity", "Basic Views Activity", "No Activity"]),
        ("Which Android Studio target requires USB debugging?", "Real device", ["Emulator", "Layout Editor", "Device Manager"]),
        ("Which prerequisites are named for Android Studio?", "JDK and Android Studio", ["Kotlin and Gradle only", "USB cable and emulator only", "Java and SQLite only"]),
        ("Which project form field selects Java or Kotlin?", "Language", ["Name", "Minimum SDK", "Save location"]),
        ("Which tool creates an emulator in the M2 steps?", "Device Manager", ["Layout Editor", "Status Bar", "Navigation Bar"]),
        ("Which project form field sets the oldest supported API?", "Minimum SDK", ["Package name", "Language", "Save location"]),
        ("Which project form option is checked in the written steps?", "Use AndroidX artifacts", ["Use raw assets", "Use Compose only", "Use Kotlin only"]),
        ("Which IDE part opens a layout file in the Layout Editor?", "Editor Window", ["Status Bar", "Toolbar", "Navigation Bar"]),
        ("Which IDE part reports warnings and messages?", "Status Bar", ["Toolbar", "Navigation Bar", "Tool Window Bar"]),
    ],
    ("MobProg", 3): [
        ("Which Kotlin modifier lets a class be inherited?", "open", ["lateinit", "val", "var"]),
        ("Which Kotlin symbol asserts a value is not null?", "!!", ["?", "//", "::"]),
        ("Which shortcut converts a Java file to Kotlin in the slides?", "Ctrl+Alt+Shift+K", ["Ctrl+Alt+K", "Ctrl+Shift+K", "Alt+Shift+K"]),
        ("What is the corrected reading of the Kotlin comparison slide's exception row?", "No checked exceptions", ["Kotlin removed all exceptions", "Only checked exceptions", "No exception handling"]),
    ],
    ("MobProg", 4): [
        ("Which directory is preferred for property animation XML?", "animator/", ["anim/", "layout/", "drawable/"]),
        ("Which directory is described for tween animation XML?", "anim/", ["animator/", "layout/", "values/"]),
        ("How are files in assets/ accessed?", "AssetManager", ["R.raw", "R.layout", "R.string"]),
    ],
    ("MobProg", 5): [
        ("Which callback marks loss of interaction as another activity comes forward?", "onPause()", ["onStop()", "onDestroy()", "onRestart()"]),
        ("Which callback marks that the activity is no longer visible?", "onStop()", ["onPause()", "onResume()", "onStart()"]),
        ("Which file declares an Activity?", "AndroidManifest.xml", ["MainActivity.kt", "activity_main.xml", "build.gradle"]),
        ("Which call loads the main layout in onCreate?", "setContentView(R.layout.activity_main)", ["setContentView(R.string.activity_main)", "findViewById(R.layout.activity_main)", "onStart(R.layout.activity_main)"]),
    ],
}


def cards_for(kind, number, ops):
    extras = [card(*row) for row in EXTRA.get((kind, number), [])]
    candidates = table_cards(ops)
    # Author-verified corrections have priority; distribute table cards across
    # all tables by their existing source order.
    chosen = extras[:]
    seen = {c["question"] for c in chosen}
    for candidate in candidates:
        if len(chosen) >= 30:
            break
        if candidate["question"] not in seen:
            chosen.append(candidate)
            seen.add(candidate["question"])
    if len(chosen) < 25:
        raise ValueError(f"Only {len(chosen)} cards for {kind} M{number}")
    return chosen


def deck(name, subject, module_numbers, all_ops, kind):
    cards = []
    # Interleave modules so a single exam session covers the whole scope.
    per_module = [cards_for(kind, n, all_ops[(kind, n)]) for n in module_numbers]
    for i in range(max(map(len, per_module))):
        cards.extend(group[i] for group in per_module if i < len(group))
    assert len({c["question"] for c in cards}) == len(cards), name
    return {"name": name, "modules_included": ", ".join(f"M{n}" for n in module_numbers),
            "subject": subject, "module_ids": None, "cards": cards}


def source_refs(kind, number):
    if kind == "StatAna":
        folder = STAT / ("sources_m1m2" if number <= 2 else "sources")
        prefix = f"M{number}" if number <= 3 else "Module_4"
    else:
        folder = MOB / "sources"
        prefix = f"Module_{number}_"
    return [p.name for p in sorted(folder.iterdir()) if p.name.startswith(prefix)] + [
        "image_slides_notes_m1m2.md" if kind == "StatAna" and number <= 2 else "image_slides_notes.md"
    ]


def main():
    m12 = load("statana_m1m2_notes", STAT / "statana_m1m2_notes.py")
    m34 = load("statana_notes", STAT / "statana_notes.py")
    mob = load("mobprog_notes", MOB / "mobprog_notes.py")
    stat_ops = split_m1m2(m12)
    stat_ops[3] = record(m34.m3)
    stat_ops[4] = record(m34.m4)
    ops = {( "StatAna", n): stat_ops[n] for n in range(1, 5)}
    ops.update({("MobProg", n): record(getattr(mob, f"module{n}")) for n in range(1, 6)})
    notes = []
    for kind, count, subject in (
        ("StatAna", 4, "Statistical Analysis and Modeling"),
        ("MobProg", 5, "Mobile Programming"),
    ):
        for n in range(1, count + 1):
            notes.append(note(f"{kind} Module {n} Reviewer Notes", subject, ops[(kind, n)], source_refs(kind, n)))
    decks = [
        deck("StatAna_M3-M4_Summative2_Verified", "Statistical Analysis and Modeling", [3, 4], ops, "StatAna"),
        deck("StatAna_M1-M4_Midterm_Verified", "Statistical Analysis and Modeling", [1, 2, 3, 4], ops, "StatAna"),
        deck("MobProg_M1-M5_Midterm_Verified", "Mobile Programming", [1, 2, 3, 4, 5], ops, "MobProg"),
    ]
    OUT.mkdir(exist_ok=True)
    (OUT / "notes_statana_mobprog.json").write_text(json.dumps(notes, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / "decks_statana_mobprog.json").write_text(json.dumps(decks, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Exported {len(notes)} notes and {len(decks)} decks: {[len(d['cards']) for d in decks]} cards")


if __name__ == "__main__":
    main()
