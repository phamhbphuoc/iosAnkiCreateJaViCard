from src.constants.urls import SEARCH_URL


def call_search_api(session, query, type, dict="javi", page=1, limit=0):

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
    }

    # JSON payload for the POST request
    payload = {
        "query": query,
        "type": type,
        "dict": dict,
        "page": page,
        "limit": limit
    }

    res = session.post(SEARCH_URL, headers=headers,
                       json=payload,
                       verify=True,)

    return res.json()
