def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short = word.replace('-', '')
    if len(short) == 10 and short.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key