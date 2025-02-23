from src.models.word import Word
import urllib.parse


def make_url_scheme(word_payload: Word, deck: str) -> str:

    word = word_payload.get("word", "")
    mean = word_payload.get("mean", "")
    phonetic = word_payload.get("phonetic", "")
    am_han_viet_list = word_payload.get("am_han_viet_list", [])
    examples = word_payload.get("examples", [])

    am_han_viet_list_str = "\n".join(am_han_viet_list)

    examples_str_list = [
        f"""{example.get("content", "")}\n{example.get("mean", "")}"""
        for example in examples
    ]
    examples_str = "\n\n".join(examples_str_list)

    front = word

    back = f"""
    {phonetic}

    [{am_han_viet_list_str}]

    {mean}
    
    {examples_str}
    """.strip()

    url_scheme = f"anki://x-callback-url/addnote?profile=User%201&type=Basic&deck={deck}&fldFront={front}&fldBack={back}"
    url_scheme = urllib.parse.quote(url_scheme)
    return url_scheme
