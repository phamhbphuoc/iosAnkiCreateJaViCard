# %%
import argparse

from src.utils.make_url_scheme import make_url_scheme
from src.utils.make_word_payload import make_word_payload


def process(query, deck): 
    word_payload = make_word_payload(query)
    url_scheme = make_url_scheme(word_payload, deck)
    return url_scheme

def main():
    # declare arguments
    parser = argparse.ArgumentParser(description="Get user input from command line.")
    parser.add_argument('--query', type=str, help='Japanese word to look up', required=True)
    parser.add_argument('--deck', type=str, help='Name of Anki deck', required=True)
    
    # parse arguments
    args = parser.parse_args()
    query = args.query
    deck = args.deck
    
    # generate url_scheme to create ios anki deck
    url_scheme = process(query, deck)
    
    print(url_scheme)
    
    return url_scheme

# Entry point of the script
if __name__ == "__main__":
    main()



# %%
