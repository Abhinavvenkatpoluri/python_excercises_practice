import string

def abbreviate(words):
    words = words.replace("-", " ")

    cleaned = ""

    for char in words:
        if char not in string.punctuation:
            cleaned += char

    acronym = ""

    for word in cleaned.split():
        acronym += word[0]

    return acronym.upper()