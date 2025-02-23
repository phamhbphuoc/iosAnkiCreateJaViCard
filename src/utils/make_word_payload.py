from src.utils.process_kanji import fetch_and_process_kanji
from src.utils.process_word import fetch_and_parse_word

def make_word_payload(query):
    
    import requests

    session = requests.Session()
    
    word_payload = fetch_and_parse_word(session, query)
    am_han_viet_list = fetch_and_process_kanji(session, query)
    word_payload["am_han_viet_list"] = am_han_viet_list

    return word_payload
