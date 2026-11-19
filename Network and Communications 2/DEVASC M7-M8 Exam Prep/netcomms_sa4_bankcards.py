"""Turn the literal question bank into AndyHub multiple choice cards (question text and answers verbatim).

Single-answer items keep their four original choices. 'Choose two/three' items become one card whose options are
answer combinations, because a card holds one correct option: the correct combination is the full set of correct
answers, the wrong options are other combinations of the original choices of the same size.
"""
import itertools
import random

from netcomms_sa4_bank import load


def _combos(choices, correct, rnd):
    size = len(correct)
    right = frozenset(correct)
    others = [frozenset(c) for c in itertools.combinations(choices, size) if frozenset(c) != right]
    rnd.shuffle(others)
    # prefer wrong combos that share one correct answer (the realistic confusions), then any other
    others.sort(key=lambda c: -len(c & right))
    wrong = others[:3]
    order = {c: i for i, c in enumerate(choices)}

    def text(combo):
        return "; ".join(sorted(combo, key=order.get))

    return text(right), [text(c) for c in wrong]


def bank_cards(seed=5):
    rnd = random.Random(seed)
    cards = []
    for item in load():
        if item["type"] != "mcq":
            continue
        question = item["question"].strip()
        if item.get("exhibit_image_url"):
            question += " (Exhibit image not shown; see the reviewer note.)"
        choices, correct = item["choices"], item["correct_answers"]
        if len(correct) == 1:
            right = correct[0].strip()
            wrong = [c.strip() for c in choices if c not in correct]
        else:
            right, wrong = _combos(choices, correct, rnd)
        wrong = wrong[:3]
        assert len(wrong) == 3 and right not in wrong, item["id"]
        cards.append((question, right, wrong))
    return cards
