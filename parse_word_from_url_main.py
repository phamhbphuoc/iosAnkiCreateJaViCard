import sys

from src.utils.parse_word_from_url import parse_word_from_url

def main():
    url = sys.argv[1]

    # get word from online dict url
    word = parse_word_from_url(url, do_unquote=True)

    print(word, end="")

    return word


# Entry point of the script
if __name__ == "__main__":
    main()