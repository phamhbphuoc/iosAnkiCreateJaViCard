import difflib

from src.utils.call_search_api import call_search_api
from src.utils.process_kanji import get_results


def parse_kanji_kana_sentence(kanji_sentence, kana_sentence):
    # Get the difference between the sentences
    diff = difflib.ndiff(kanji_sentence, kana_sentence)

    # Initialize variables
    furigana_sentence = ""
    kanji_part = ""
    kana_part = ""

    # Iterate over the diff list
    for char in diff:
        if char.startswith(
            "-"
        ):  # This means the character is in kanji_sentence but not kana_sentence (Kanji)
            kanji_part += char[2:]
        elif char.startswith(
            "+"
        ):  # This means the character is in kana_sentence but not kanji_sentence (Kana)
            kana_part += char[2:]
        elif char.startswith(" "):  # Characters that are the same in both sentences
            # When we encounter a space, and have completed a pair of kanji and kana, add them to result, and clear pair of kanji and kana
            if kanji_part and kana_part:
                furigana_sentence += f"<ruby>{kanji_part}<rt>{kana_part}</rt></ruby>"
                kanji_part = ""  # Reset the kanji part for the next pair
                kana_part = ""  # Reset the kana part for the next pair
            # Add normal character
            furigana_sentence += char[2:]

    # Handle the case where the last pair might not be followed by a space
    if kanji_part and kana_part:
        furigana_sentence += f"<ruby>{kanji_part}<rt>{kana_part}</rt></ruby>"

    return furigana_sentence


def fetch_and_parse_examples(session, query):

    res = call_search_api(session, query, type="example", limit=5)
    results = get_results(res)
    return results
