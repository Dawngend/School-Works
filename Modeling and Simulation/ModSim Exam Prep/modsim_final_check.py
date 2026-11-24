"""Build the ModSim final reviewer and AndyHub deck from the six cited modules.

Run after final_M1.json through final_M6.json are present. PDF page numbers are
one-based physical pages. Optional matlab_checks on a section or card consist
of {"expression": "...", "expected": "..."}; expressions may include MATLAB
statements followed by an expression. Computed MATLAB results in the content
must have corresponding checks. This validates citations and executable checks,
not the semantic correctness of natural-language paraphrases.
"""
import hashlib
import json
import heapq
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = Path('D:/School-Works/Modeling and Simulation/ModSim Exam Prep/sources')
MATLAB = Path('D:/bin/matlab.exe')
OUTPUT = HERE.parent / 'PAMESA - ModSim Final Reviewer'
EXPORT = ROOT / 'AndyHub Export' / 'payload_modsim_final.json'
SIDECAR = HERE / 'modsim_final_sources.json'
TITLE = 'ModSim Final Reviewer'
SUBJECT = 'Modeling and Simulation'
sys.path.insert(0, str(ROOT / 'Network and Communications 2' / 'DEVASC M3-M4 Exam Prep'))
from notes_lib import Notes
from modsim_notes import save_pdf


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f'{label} must be nonempty text')
    return value


def normalized(value):
    return ' '.join(value.casefold().split())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_checks(item, where):
    checks = item.get('matlab_checks', [])
    require(isinstance(checks, list), f'{where}: matlab_checks must be a list')
    for check in checks:
        require(isinstance(check, dict), f'{where}: invalid MATLAB check')
        text(check.get('expression'), f'{where} MATLAB expression')
        text(check.get('expected'), f'{where} MATLAB expected')
    return checks


def load_modules():
    modules = []
    for number in range(1, 7):
        module = f'M{number}'
        path = HERE / f'final_{module}.json'
        data = json.loads(path.read_text(encoding='utf-8-sig'))
        require(isinstance(data, dict) and data.get('module') == module, f'{path}: wrong module')
        filename = text(data.get('source_file'), f'{module} source_file')
        require(Path(filename).name == filename and filename.lower().endswith('.pdf'), f'{module}: invalid source filename')
        source = SOURCE / filename
        require(source.is_file(), f'{module}: missing source {source}')
        pdf = PdfReader(str(source))
        page_text = [(page.extract_text() or '').strip() for page in pdf.pages]
        require(page_text and any(page_text), f'{module}: source has no extractable text')
        for field in ('sections', 'cards'):
            require(isinstance(data.get(field), list) and data[field], f'{module}: empty {field}')
            for index, item in enumerate(data[field], 1):
                where = f'{module} {field} {index}'
                require(isinstance(item, dict), f'{where}: expected object')
                pages = item.get('pages')
                require(isinstance(pages, list) and pages and all(type(p) is int and 1 <= p <= len(page_text) for p in pages), f'{where}: invalid PDF pages')
                require(len(set(pages)) == len(pages), f'{where}: repeated page')
                # Image-heavy slides can contain no text: record this honestly for review.
                validate_checks(item, where)
                if field == 'sections':
                    text(item.get('heading'), f'{where} heading')
                    paragraphs = item.get('paragraphs')
                    require(isinstance(paragraphs, list) and paragraphs, f'{where}: empty paragraphs')
                    for paragraph in paragraphs:
                        text(paragraph, where)
                else:
                    text(item.get('question'), f'{where} question')
                    options = item.get('options')
                    require(isinstance(options, list) and len(options) == 4, f'{where}: expected four options')
                    for option in options:
                        text(option, f'{where} option')
                    require(len({normalized(o) for o in options}) == 4, f'{where}: duplicate options')
                    require(sum(o == item.get('correct_answer') for o in options) == 1, f'{where}: answer must match exactly one option')
        modules.append({'data': data, 'source': source, 'page_text': page_text,
                        'sha256': digest(source), 'input_sha256': digest(path)})
    return modules


def select_cards(modules):
    # Visit midpoints of the largest remaining intervals first, so partial
    # selection samples the entire source list rather than only its prefix.
    def spread(cards):
        pending = [(-len(cards), 0, len(cards))]
        result = []
        while pending:
            _, start, end = heapq.heappop(pending)
            middle = (start + end - 1) // 2
            result.append(middle)
            for lo, hi in ((start, middle), (middle + 1, end)):
                if lo < hi:
                    heapq.heappush(pending, (-(hi - lo), lo, hi))
        return result
    candidates = [(module, card, index) for module in modules
                  for index, card in enumerate(module['data']['cards'], 1)]
    selected, seen = [], set()
    for index in spread(candidates):
        module, card, source_index = candidates[index]
        key = normalized(card['question'])
        if key not in seen:
            seen.add(key)
            selected.append((module, card, source_index))
            if len(selected) == 200:
                break
    require(len(selected) == 200, f'Only {len(selected)} unique questions available; 200 required')
    require(len({m['data']['module'] for m, _, _ in selected}) == 6, 'Deck must cover all six modules')
    return selected


def verify_matlab(modules, selected):
    checks = []
    for module in modules:
        for index, section in enumerate(module['data']['sections'], 1):
            checks.extend((module['data']['module'], f'section {index}', check)
                          for check in validate_checks(section, 'section'))
    for module, card, index in selected:
        checks.extend((module['data']['module'], f'card {index}', check)
                      for check in validate_checks(card, 'card'))
    if not checks:
        return {'status': 'not_applicable', 'checks': [], 'description': 'No explicit MATLAB output checks supplied; no MATLAB execution claimed.'}
    require(MATLAB.is_file(), f'MATLAB is required for {len(checks)} explicit output checks: {MATLAB}')
    def quote(value):
        return value.replace("'", "''")
    commands = []
    for i, (_, _, check) in enumerate(checks, 1):
        # eval allows an expression containing setup statements and a final value.
        commands.append("clear; actual = eval('%s'); expected = eval('%s'); "
                        "assert(isequaln(actual, expected) || (isnumeric(actual) && isnumeric(expected) && "
                        "isequal(size(actual),size(expected)) && all(abs(actual(:)-expected(:)) <= "
                        "1e-10 * max(1,abs(expected(:))))),'MATLAB check %d failed');" %
                        (quote(check['expression']), quote(check['expected']), i))
    with tempfile.TemporaryDirectory(dir=HERE) as directory:
        script = Path(directory) / 'checks.m'
        script.write_text('\n'.join(commands), encoding='utf-8')
        result = subprocess.run([str(MATLAB), '-batch', "run('%s')" % quote(str(script))],
                                capture_output=True, text=True, timeout=600)
    require(result.returncode == 0, f'MATLAB verification failed:\n{result.stdout}\n{result.stderr}')
    return {'status': 'passed', 'executable': str(MATLAB), 'checks': [
        {'module': module, 'item': item, **check} for module, item, check in checks]}


def citation(module, pages):
    return f"{module['data']['source_file']}, PDF p. " + ', '.join(map(str, pages))


def build(modules, selected, matlab):
    notes = Notes(TITLE, 'Modules 1–6 | Slide-based review')
    note_sections = []
    section_sources = []
    for module in modules:
        data = module['data']
        notes.h1(data['module'])
        for index, section in enumerate(data['sections'], 1):
            ref = citation(module, section['pages'])
            notes.h2(section['heading'])
            for paragraph in section['paragraphs']:
                notes.p(paragraph)
            notes.p('Source: ' + ref)
            note_sections.append({'heading': f"{data['module']}: {section['heading']}",
                                  'summary': '\n\n'.join(section['paragraphs']),
                                  'key_terms': [], 'properties': [], 'worked_examples': [],
                                  'common_mistakes': [], 'source_refs': [ref],
                                  'memory_aids': [], 'comparisons': []})
            section_sources.append({'module': data['module'], 'section_index': index,
                                    'heading': section['heading'], 'source_file': data['source_file'],
                                    'pages': section['pages']})
    notes.doc.save(str(OUTPUT.with_suffix('.docx')))
    save_pdf(notes.doc, OUTPUT.with_suffix('.pdf'))
    cards, card_sources = [], []
    for deck_index, (module, card, source_index) in enumerate(selected, 1):
        cards.append({'type': 'multiple_choice', 'question': card['question'],
                      'correct_answer': card['correct_answer'],
                      'options': json.dumps(card['options'], ensure_ascii=False), 'times_missed': 0})
        card_sources.append({'deck_index': deck_index, 'module': module['data']['module'],
                             'module_card_index': source_index, 'question': card['question'],
                             'source_file': module['data']['source_file'], 'pages': card['pages']})
    payload = {'notes': [{'title': TITLE, 'subject': SUBJECT, 'module_ids': [],
                          'content': {'sections': note_sections, 'formula_sheet': [], 'self_check': [], 'cram_sheet': []}}],
               'decks': [{'name': 'ModSim Final Flashcards', 'subject': SUBJECT,
                          'modules_included': 'M1, M2, M3, M4, M5, M6', 'module_ids': None, 'cards': cards}]}
    EXPORT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    source_metadata = []
    for module in modules:
        referenced = sorted({page for item in module['data']['sections'] for page in item['pages']} |
                            {page for m, card, _ in selected if m is module for page in card['pages']})
        source_metadata.append({'module': module['data']['module'], 'source_file': module['data']['source_file'],
                                'source_sha256': module['sha256'], 'module_json_sha256': module['input_sha256'],
                                'pdf_page_count': len(module['page_text']),
                                'referenced_pages': [{'page': p, 'extractable_text_characters': len(module['page_text'][p-1]),
                                                      'text_sha256': hashlib.sha256(module['page_text'][p-1].encode('utf-8')).hexdigest()}
                                                     for p in referenced]})
    sidecar = {'title': TITLE, 'source_directory': str(SOURCE), 'sources': source_metadata,
               'sections': section_sources, 'cards': card_sources,
               'verification': {'card_count': len(cards), 'unique_normalized_questions': len({normalized(c['question']) for c in cards}),
                                'module_card_counts': dict(sorted(Counter(m['data']['module'] for m, _, _ in selected).items())),
                                'citation_page_bounds': 'passed', 'card_shape_and_answers': 'passed',
                                'pdf_text': 'Extracted per page; zero-length text may indicate an image slide and is not semantic verification.',
                                'semantic_review': 'Not automatically established by page or text extraction checks.',
                                'matlab': matlab}}
    SIDECAR.write_text(json.dumps(sidecar, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    validate_outputs(modules, selected, matlab)


def validate_outputs(modules, selected, matlab):
    """Reopen the actual deliverables and check their structure and citations."""
    from docx import Document
    doc = Document(str(OUTPUT.with_suffix('.docx')))
    require(any(p.text.strip() for p in doc.paragraphs), 'DOCX has no readable text')
    pdf = PdfReader(str(OUTPUT.with_suffix('.pdf')))
    require(pdf.pages and all((page.extract_text() or '').strip() for page in pdf.pages),
            'Reviewer PDF has an empty or unreadable page')
    payload = json.loads(EXPORT.read_text(encoding='utf-8'))
    sidecar = json.loads(SIDECAR.read_text(encoding='utf-8'))
    require(len(payload['notes']) == len(payload['decks']) == 1, 'Expected one note and one deck')
    note, deck = payload['notes'][0], payload['decks'][0]
    require(note['title'] == TITLE and note['subject'] == SUBJECT and note['module_ids'] == [],
            'Invalid note metadata')
    require(deck['name'] == 'ModSim Final Flashcards' and deck['subject'] == SUBJECT and
            deck['modules_included'] == 'M1, M2, M3, M4, M5, M6' and deck['module_ids'] is None,
            'Invalid deck metadata')
    hub = Path('D:/Personal Projects/All In One Reviewer')
    if hub.is_dir():
        sys.path.insert(0, str(hub))
        try:
            from andyhub_api.schemas import NoteContent
        except ImportError:
            pass
        else:
            NoteContent.model_validate(note['content'])
    require(sidecar['title'] == TITLE and sidecar['verification']['matlab'] == matlab,
            'Invalid sidecar metadata')
    sections = note['content']['sections']
    expected_sections = [(m, s) for m in modules for s in m['data']['sections']]
    require(len(sections) == len(sidecar['sections']) == len(expected_sections), 'Section count mismatch')
    for exported, ref, (module, section) in zip(sections, sidecar['sections'], expected_sections):
        require(exported['source_refs'] == [citation(module, section['pages'])] and
                ref['module'] == module['data']['module'] and ref['source_file'] == module['data']['source_file'] and
                ref['pages'] == section['pages'], 'Section citation mismatch')
    cards = deck['cards']
    require(len(cards) == len(sidecar['cards']) == len(selected) == 200, 'Card count mismatch')
    require(len({normalized(card['question']) for card in cards}) == 200, 'Duplicate exported questions')
    for index, (card, ref, (module, original, source_index)) in enumerate(zip(cards, sidecar['cards'], selected), 1):
        options = json.loads(card['options'])
        require(card['type'] == 'multiple_choice' and card['times_missed'] == 0 and
                card['question'] == original['question'] and options == original['options'] and
                len(options) == 4 and len({normalized(o) for o in options}) == 4 and
                sum(o == card['correct_answer'] for o in options) == 1 and
                card['correct_answer'] == original['correct_answer'], f'Invalid exported card {index}')
        require(ref['deck_index'] == index and ref['module_card_index'] == source_index and
                ref['question'] == card['question'] and ref['module'] == module['data']['module'] and
                ref['source_file'] == module['data']['source_file'] and ref['pages'] == original['pages'],
                f'Invalid card citation {index}')
    require({ref['module'] for ref in sidecar['cards']} == {f'M{i}' for i in range(1, 7)},
            'Card module coverage incomplete')


def main():
    modules = load_modules()
    selected = select_cards(modules)
    matlab = verify_matlab(modules, selected)
    build(modules, selected, matlab)
    print(f'Built reviewer and {len(selected)} cards; MATLAB: {matlab["status"]}.')


if __name__ == '__main__':
    main()
