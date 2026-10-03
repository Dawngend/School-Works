import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJECT_DIR = os.path.dirname(HERE)
HUB = r"D:\Personal Projects\All In One Reviewer"
sys.path.insert(0, HERE)
sys.path.insert(0, HUB)

from build_lib import M, Q, build, to_pdf
from cards_data import KEEP_M3, KEEP_M4, KEEP_MOCK, M3_NEW, M4_NEW

decks = json.load(open(os.path.join(HERE, "andyhub_decks.json"), encoding="utf-8"))
mock_raw = json.load(open(os.path.join(HERE, "andyhub_mock.json"), encoding="utf-8"))["cards"]
by_id = {}
for deck in decks.values():
    for c in deck["cards"]:
        by_id[c[0]] = c
for c in mock_raw:
    by_id[c[0]] = c


def from_hub(ids):
    out = []
    for i in ids:
        c = by_id[i]
        opts = json.loads(c[5])
        wrong = [o for o in opts if o != c[4]]
        out.append((c[3], c[4], wrong, "Scenario question; matches the slide wording"))
    return out


m3_concept, m4_concept = M3_NEW, M4_NEW
m3_scen, m4_scen, mock_scen = from_hub(KEEP_M3), from_hub(KEEP_M4), from_hub(KEEP_MOCK)

rnd = random.Random(11)
extra_m3 = rnd.sample(m3_concept, 11)
extra_m4 = rnd.sample(m4_concept, 10)
mock_cards = mock_scen + extra_m3 + extra_m4
rnd.shuffle(mock_cards)


def qs(cards):
    return [Q(*c) for c in cards]


M3_MATCH = [
    M("Match the Agile or Scrum term with its description.",
      [("Story", "A simple statement of what a user needs and why"),
       ("Scrum team", "Uses stand-up meetings to review progress"),
       ("Sprint", "A time-boxed period where working software is developed"),
       ("Backlog", "A prioritized list of all the features for the software")],
      ["A list of resolved bugs"], "Agile Methods slides"),
    M("Match the SDLC phase with its result.",
      [("Requirements and Analysis", "Software Requirement Specification (SRS)"),
       ("Design", "High-Level and Low-Level Design documents"),
       ("Implementation", "Functional code ready to be tested"),
       ("Deployment", "The final software is released to end users")],
      ["A signed contract"], "SDLC phase slides"),
    M("Match the Git command with its purpose.",
      [("git init", "Creates a new empty repository (.git directory)"),
       ("git clone", "Gets an existing repository"),
       ("git add", "Adds files to the staging area"),
       ("git commit", "Updates the local repository with the staged changes"),
       ("git push", "Updates the remote repository")],
      ["Deletes a branch"], "Git Commands slides"),
    M("Match the .diff symbol with its meaning.",
      [("+", "The line has been added"), ("-", "The line has been removed"),
       ("@@", "The next block of information is starting"),
       ("/dev/null", "A file has been added or removed")],
      ["Context lines"], ".diff Files slide"),
    M("Match the MVC component with its role.",
      [("Model", "The application's data structure; manages data, logic, and rules"),
       ("View", "The visual representation of the data"),
       ("Controller", "The middleman that takes user input and formats it for the model or view")],
      ["Stores a list of observers"], "MVC slide"),
]
M4_MATCH = [
    M("Match the RESTful API method with its CRUD function.",
      [("GET", "READ"), ("POST", "CREATE"), ("DELETE", "DELETE"), ("PUT/PATCH", "UPDATE")], ["ERASE"], "HTTP method table"),
    M("Match the rate limit algorithm with its description.",
      [("Leaky bucket", "Requests enter a queue and are processed at a fixed rate"),
       ("Token bucket", "Each user gets a defined number of tokens per time increment"),
       ("Fixed window counter", "A counter is assigned to a fixed window of time"),
       ("Sliding window counter", "Counts requests from the beginning of the window to the current time")],
      ["Requests are compressed"], "Rate Limit Algorithms slides"),
    M("Match the HTTP status code with its meaning.",
      [("401", "No valid authentication credentials"), ("403", "Understood but rejected by the server"),
       ("404", "Resource path not found on the server"), ("500", "Internal server error"),
       ("503", "Service unavailable")],
      ["Resource created"], "Common status codes"),
    M("Match the REST constraint with its description.",
      [("Stateless", "The server cannot contain session states"),
       ("Cache", "Responses must state whether they are cacheable"),
       ("Client-server", "Client and server are independent of each other"),
       ("Code-on-demand", "Optional; responses may include executable code")],
      ["Each layer serves only the layer below"], "REST constraints slides"),
    M("Match the SOAP element with its role.",
      [("Envelope", "The root element of the XML document"),
       ("Header", "Application-specific information such as authorization"),
       ("Body", "The data to be transported to the recipient"),
       ("Fault", "Error and/or status information")], ["The prologue"], "SOAP slide"),
]

RUN = [
    ("PAMESA - NetComms 2 M3 Reviewer", "NetComms 2 Module 3 Reviewer: Software Development and Design",
     "DevNet Associate, Module 3. Built from DEVASC_Module_3.pdf. Choice and matching only.",
     [("Concept Questions (Slide Order)", qs(m3_concept)), ("Scenario Questions", qs(m3_scen)),
      ("Matching (Dropdown Style)", M3_MATCH)], 21),
    ("PAMESA - NetComms 2 M4 Reviewer", "NetComms 2 Module 4 Reviewer: Understanding and Using APIs",
     "DevNet Associate, Module 4. Built from DEVASC_Module_4.pdf. Choice and matching only.",
     [("Concept Questions (Slide Order)", qs(m4_concept)), ("Scenario Questions", qs(m4_scen)),
      ("Matching (Dropdown Style)", M4_MATCH)], 22),
]
mock_match = [M3_MATCH[0], M3_MATCH[4], M4_MATCH[0], M4_MATCH[1]]
RUN.append((
    "PAMESA - NetComms 2 SA2 Mock Exam", "NetComms 2 Summative 2 Mock Exam: Modules 3 and 4",
    "50 items: choice questions plus dropdown matching. Answer key at the end.",
    [("Part 1: Multiple Choice", qs(mock_cards[:46])), ("Part 2: Matching", mock_match)], 23))

for name, title, sub, sections, seed in RUN:
    path = os.path.join(SUBJECT_DIR, name + ".docx")
    n, key = build(path, title, sub, sections, seed=seed)
    pdf = to_pdf(path)
    print(name, "items:", n, "->", os.path.basename(pdf))

# Verified AndyHub decks (local DB): curated hub cards plus the new slide-literal cards.
if os.environ.get("SKIP_DB"):
    sys.exit(0)
os.chdir(HUB)
import database
from repositories import NewCard

database.init_db()


def make_deck(name, modules, cards):
    r = random.Random(5)
    new = []
    for q, correct, wrong, _ in cards:
        opts = [correct] + list(wrong)
        r.shuffle(opts)
        new.append(NewCard("multiple_choice", q, correct, opts))
    return database.create_deck_with_cards(name, modules, "Network and Communications 2", new)


ids = {
    "M3": make_deck("DEVASC Module 3 (Verified)", "DEVASC_Module_3.pdf", m3_concept + m3_scen),
    "M4": make_deck("DEVASC Module 4 (Verified)", "DEVASC_Module_4.pdf", m4_concept + m4_scen),
    "Mock": make_deck("DEVASC Mock Exam M3 and M4 (Verified)", "DEVASC_Module_3.pdf, DEVASC_Module_4.pdf", mock_cards),
}
print("deck ids", ids, "counts", len(m3_concept + m3_scen), len(m4_concept + m4_scen), len(mock_cards))
