from src.models.word import Word
import urllib.parse


def make_url_scheme(word_payload: Word, deck: str) -> str:

    word = word_payload.get("word", "")
    mean = word_payload.get("mean", "")
    phonetic = word_payload.get("phonetic", "")
    am_han_viet_list = word_payload.get("am_han_viet_list", [])
    examples = word_payload.get("examples", [])

    am_han_viet_list_str = "<br>".join(am_han_viet_list)

    examples_str_list = [
        f"""{example.get("content", "")}\n<br>\n{example.get("mean", "")}"""
        for example in examples
    ]
    examples_str = "\n<br><br>\n".join(examples_str_list)

    deck = urllib.parse.quote(deck)

    front = urllib.parse.quote(word)

    back = f"""
{phonetic}
<br><br>
[{am_han_viet_list_str}]
<br><br>
{mean}
{f"<br><br>" if examples_str else ""}
{examples_str}
""".strip()
    back = urllib.parse.quote(back)

    url_scheme = f"anki://x-callback-url/addnote?profile=User%201&type=Basic&deck={deck}&fldFront={front}&fldBack={back}"
    return url_scheme
