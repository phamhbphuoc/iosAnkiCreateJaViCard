from urllib.parse import urlparse, unquote

def parse_word_from_url(url, do_unquote=False):

    # Parse the URL and extract the path
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Extract the encoded word after the last '/'
    word = path.split('/')[-1]

    if do_unquote:
        # Decode the encoded word
        word = unquote(word)

    return word
