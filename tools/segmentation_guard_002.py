"""Shared structural guard for SEGMENTATION-002 (corpus-wide U+200B break opportunities).

Used by both the proposal generator (tools/segment_corpus_002.py, runs offline with PyThaiNLP)
and the candidate builder (tools/build_fresh_translation_007.py, runs on Windows with UnityPy).
Cuts are Unicode-codepoint offsets into the ORIGINAL text. Stripping U+200B from the marked
text must reproduce the original literally. This guard is structural only; it does not
validate Thai word meaning.
"""
import hashlib
import re
import unicodedata

ZWSP = '​'
THAI = re.compile(r'[ก-๛]')
# Tokens, rich-text tags, I2 markers, Latin/number runs (incl. inner spaces/slashes/hyphens).
PROTECTED = re.compile(r'\{[^{}]*\}|<[^<>]*>|\[i2[^\]]*\]|[A-Za-z0-9]+(?:[ /\-.:_][A-Za-z0-9]+)*')
SYNTAX = re.compile(r'\{[^{}]*\}|<[^<>]*>|\[i2[^\]]*\]')
LEADING_VOWELS = 'เแโใไ'                  # must not end a line
NO_BREAK_BEFORE = 'ะาำๅๆฯ'  # ะ า ำ ๅ ๆ ฯ (attach to preceding syllable)
NO_BREAK_AFTER = 'ั็'          # ั ็ require a following consonant in the same syllable
CLOSE_PUNCT = ')]}"\'”’.,;:!?%»'           # never start a line with these
OPEN_PUNCT = '([{"\'“‘«'                  # never end a line with these

sha = lambda data: hashlib.sha256(data).hexdigest()


def cut_reason(text, cut):
    """Return None if a cut at this codepoint offset is structurally acceptable, else a reason."""
    if type(cut) is not int or not 0 < cut < len(text):
        return 'out_of_range'
    prev, nxt = text[cut - 1], text[cut]
    if prev.isspace() or nxt.isspace():
        return 'whitespace_adjacent'
    if prev in LEADING_VOWELS:
        return 'after_leading_vowel'
    if unicodedata.category(nxt).startswith('M'):
        return 'before_combining_mark'
    if nxt in NO_BREAK_BEFORE:
        return 'before_trailing_vowel_or_repeat'
    if prev in NO_BREAK_AFTER:
        return 'after_open_syllable_sign'
    if nxt in CLOSE_PUNCT:
        return 'before_closing_punct'
    if prev in OPEN_PUNCT:
        return 'after_opening_punct'
    if not (THAI.match(prev) and THAI.match(nxt)):
        return 'not_thai_thai_boundary'
    for m in PROTECTED.finditer(text):
        if m.start() < cut < m.end():
            return 'inside_protected_run'
    return None


def validate(text, cuts, expected_hash):
    """Raise ValueError on any unsafe/stale cut; return the marked text."""
    if ZWSP in text:
        raise ValueError('Source already contains U+200B')
    if sha(text.encode('utf-8')) != expected_hash:
        raise ValueError('Underlying source hash changed')
    if list(cuts) != sorted(set(cuts)):
        raise ValueError('Cuts duplicate/unsorted')
    for cut in cuts:
        reason = cut_reason(text, cut)
        if reason:
            raise ValueError('Unsafe cut %r at %d: %s' % (text[max(0, cut - 6):cut + 6], cut, reason))
    cutset = set(cuts)
    marked = ''.join((ZWSP if i in cutset else '') + c for i, c in enumerate(text))
    if marked.replace(ZWSP, '') != text:
        raise ValueError('Underlying equality failed')
    if SYNTAX.findall(marked) != SYNTAX.findall(text):
        raise ValueError('Token/tag sequence changed')
    if marked.count('\n') != text.count('\n') or marked.count('\t') != text.count('\t'):
        raise ValueError('Line structure changed')
    return marked


def self_test():
    fixtures = [('token', '{STAFF_COUNT_LIMIT}', [4]), ('rich_tag', '<color=red>คำ</color>', [4]),
                ('combining_mark', 'กี่', [1]), ('leading_vowel', 'เรียน', [1]),
                ('Latin_run', 'MSAA Samples', [2]), ('source_LF', 'ก\nข', [1]),
                ('duplicate_cut', 'กขค', [1, 1]), ('sara_am', 'ต่ำ', [2]), ('sara_am_tone', 'ต่ำ', [1]),
                ('sara_a', 'ชนะ', [2]), ('mai_yamok', 'ซ้ำๆ', [3]), ('mai_han_akat', 'วันนี้', [2]),
                ('close_quote', 'ก"ข', [1]), ('open_quote', 'ก"ข', [2]), ('thai_latin', 'ระดับCPU', [5])]
    for name, text, cuts in fixtures:
        try:
            validate(text, cuts, sha(text.encode('utf-8')))
        except ValueError:
            continue
        raise AssertionError('Unsafe cut accepted: ' + name)
    try:
        validate('กขค', [1], sha('กขง'.encode('utf-8')))
    except ValueError:
        pass
    else:
        raise AssertionError('Source mutation accepted')
    assert validate('รอบวิทยาเขต', [3], sha('รอบวิทยาเขต'.encode('utf-8'))) == 'รอบ​วิทยาเขต'
    assert validate('ต่ำและมี', [3, 6], sha('ต่ำและมี'.encode('utf-8'))) == 'ต่ำ​และ​มี'
    return len(fixtures) + 1


if __name__ == '__main__':
    print('negative controls rejected:', self_test())
