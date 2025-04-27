from stats import get_num_words
from stats import get_book_text
from stats import get_num_chars_lower
from stats import sort_chars

import sys


def main():
    if sys.argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    wc = get_num_words(text)
    chars = get_num_chars_lower(text)
    chars = sort_chars(chars)
    fchars = ""
    for c in [f"{i['name']}: {i['num']}\n" for i in chars]:
        fchars += c
    fchars = fchars[:-1]

    print(f"""============ BOOKBOT ============
Analyzing book found at {path}
----------- Word Count ----------
Found {wc} total words
--------- Character Count -------
{fchars}
============= END ===============
""")


if __name__ == "__main__":
    main()
