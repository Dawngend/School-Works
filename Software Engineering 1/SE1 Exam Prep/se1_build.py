import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, r"D:\School-Works\Network and Communications 2\DEVASC M3-M4 Exam Prep")

from build_lib import build, to_pdf
from se1_data import M3_L, M3_M, M3_Q, M4_L, M4_M, M4_Q

rnd = random.Random(3)
mock_q = rnd.sample(M3_Q, 17) + rnd.sample(M4_Q, 17)
rnd.shuffle(mock_q)
mock_m = rnd.sample(M3_M, 2) + rnd.sample(M4_M, 2)
mock_l = rnd.sample(M3_L, 6) + rnd.sample(M4_L, 6)

RUN = [
    ("PAMESA - SE1 M3 Reviewer", "SE1 Module 3 Reviewer: Agile Methodologies",
     "CS0025 Software Engineering 1, Module 3. Built from CS0025-M3S0, M3S1, and M3S2. Choice, matching, and typed lists.",
     [("Multiple Choice and True or False", M3_Q), ("Matching (Dropdown Style)", M3_M), ("Typed Lists (Enumeration)", M3_L)], 31),
    ("PAMESA - SE1 M4 Reviewer", "SE1 Module 4 Reviewer: System Models and Requirements",
     "CS0025 Software Engineering 1, Module 4. Built from CS0025-M4S0-1, M4S1, and M4S2. Choice, matching, and typed lists.",
     [("Multiple Choice and True or False", M4_Q), ("Matching (Dropdown Style)", M4_M), ("Typed Lists (Enumeration)", M4_L)], 32),
    ("PAMESA - SE1 SA2 Mock Exam", "SE1 Summative 2 Mock Exam: Modules 3 and 4",
     "50 items: choice, dropdown matching, and typed lists. Answer key at the end.",
     [("Part 1: Multiple Choice and True or False", mock_q), ("Part 2: Matching", mock_m), ("Part 3: Typed Lists", mock_l)], 33),
]
for name, title, sub, sections, seed in RUN:
    path = os.path.join(OUT, name + ".docx")
    n, _ = build(path, title, sub, sections, seed=seed)
    to_pdf(path)
    print(name, n, "items")
