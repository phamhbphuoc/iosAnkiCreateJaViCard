# %%
import sys

from src.utils.make_url_scheme import make_url_scheme
from src.utils.make_word_payload import make_word_payload


def process(query, deck):
    word_payload = make_word_payload(query)
    url_scheme = make_url_scheme(word_payload, deck)
    return url_scheme

def main():
    query = sys.argv[1]
    deck = sys.argv[2]

    # generate url_scheme to create ios anki deck
    url_scheme = process(query, deck)

    print(url_scheme)

    return url_scheme


# Entry point of the script
if __name__ == "__main__":
    main()
