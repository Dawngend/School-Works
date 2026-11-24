import sys
sys.dont_write_bytecode = True

import itertools
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "devasc-final-200.json")


def load():
    with open(BANK, encoding="utf-8") as fh:
        return json.loads(fh.read().replace("\u2014", " - "))["items"]


def _combos(choices, correct, rnd):
    size = len(correct)
    right = frozenset(correct)
    others = [frozenset(c) for c in itertools.combinations(choices, size) if frozenset(c) != right]
    rnd.shuffle(others)
    # Prefer wrong combinations sharing the most correct answers, as in SA4.
    others.sort(key=lambda c: -len(c & right))
    wrong = others[:3]
    order = {c: i for i, c in enumerate(choices)}

    def text(combo):
        return "; ".join(sorted(combo, key=order.get))

    return text(right), [text(c) for c in wrong]


def final_cards():
    rnd = random.Random(5)
    cards = []
    for item in load():
        question = item["question"]
        if item["exhibit_text"]:
            question += " " + item["exhibit_text"]
        choices, correct = item["choices"], item["correct"]
        if len(correct) == 1:
            right = correct[0]
            wrong = [choice for choice in choices if choice not in correct][:3]
        else:
            right, wrong = _combos(choices, correct, rnd)
        assert len(wrong) in (2, 3), item["id"]
        assert len(set([right] + wrong)) == 1 + len(wrong), item["id"]
        cards.append((question, right, wrong))
    return cards
