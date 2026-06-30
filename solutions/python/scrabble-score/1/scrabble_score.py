groups = {
    1: "aeioulnrst",
    2: "dg",
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz"
}

score_map = {
    letter: value
    for value, letters in groups.items()
    for letter in letters
}

def score(word):
    return sum(score_map[ch] for ch in word.lower())
