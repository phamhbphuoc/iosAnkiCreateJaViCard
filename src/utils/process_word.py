from src.utils.call_search_api import call_search_api
from src.utils.process_example import fetch_and_parse_examples, parse_kanji_kana_sentence


def parse_word(res, session, query):

    data = res["data"]
    filtered_data = data[0] if data else {}

    means = filtered_data.get("means", "")
    filtered_means = means[0] if means else {}

    mean = filtered_means.get("mean", "")

    examples = filtered_means.get("examples") or []
    
    if (len(examples) < 1):
        examples = fetch_and_parse_examples(session, query)
    for example in examples:
        furigana_sentence = parse_kanji_kana_sentence(example.get("content"), example.get("transcription"))
        example["furigana_sentence"] = furigana_sentence

    phonetic = filtered_data.get("phonetic", "")

    return {
        "mean": mean,
        "phonetic": phonetic,
        "examples": examples,
    }


def get_nghia_han_viet(res):
    found_res = res[0] if res else {}
    detail = found_res.get("detail", "")
    return detail.split("##")


def fetch_and_parse_word(session, query):

    res = call_search_api(session, query, type="word", limit=1)
    word_payload = parse_word(res, session, query)
    word_payload["word"] = query

    return word_payload
