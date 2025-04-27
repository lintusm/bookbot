def get_num_words(st: str):
    c = 0
    for line in st.splitlines():
        for w in line.split(' '):
            if w.__len__() > 0:
                c += 1
    return c


def get_num_chars_lower(st: str) -> dict:
    chars = {}
    for c in st:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def sort_on(d):
    return d["num"]


def sort_chars(chars: dict) -> str:
    list_chars = []
    for k, v in chars.items():
        if not k.isalpha():
            continue
        list_chars.append({"name": k, "num": v})
    list_chars.sort(key=sort_on, reverse=True)
    return list_chars
