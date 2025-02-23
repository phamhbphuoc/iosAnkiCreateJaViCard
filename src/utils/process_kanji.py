from src.utils.call_search_api import call_search_api


def get_results(res):
    return res["results"]


def get_am_han_viet(filtered_result):
    return filtered_result.get("mean", "")


def get_nghia_han_viet(filtered_result):
    detail = filtered_result.get("detail", "")
    return detail.split("##")


def fetch_and_process_kanji(session, query):

    res = call_search_api(session, query, type="kanji")
    results = get_results(res)

    am_han_viet_list = [get_am_han_viet(result) for result in results]

    return am_han_viet_list
