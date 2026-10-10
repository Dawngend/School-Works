"""Self-check for the 100 items: counts, and that the AndyHub grader accepts each answer and rejects a wrong one."""
import sys
from collections import Counter

sys.path.insert(0, ".")
sys.path.insert(0, r"D:\Personal Projects\All In One Reviewer")
import ml_100_items as m
from grading import grade_enumeration, grade_problem_answer

items = m.all_items()
print(len(items), Counter(i["label"] for i in items))
bad = []
for it in items:
    if it["type"] == "problem":
        if not grade_problem_answer(it["answer"], it["answer"]).matched:
            bad.append(("self", it["answer"]))
        if grade_problem_answer("zzz_wrong", it["answer"]).matched:
            bad.append(("wrong accepted", it["answer"]))
        if not grade_problem_answer("  " + it["answer"].upper() + " ", it["answer"]).matched:
            bad.append(("case", it["answer"]))
    if it["type"] == "enumeration":
        _, missed = grade_enumeration(", ".join(it["expected"]), it["expected"])
        if missed:
            bad.append(("enum", it["q"], missed))
        _, missed = grade_enumeration("nothing relevant", it["expected"])
        if not missed:
            bad.append(("enum wrong accepted", it["q"]))
print("problems:", bad)
