def find_anagrams(word, candidates):
    word = word.lower()
    expected = []

    for candidate in candidates:
        if candidate.lower() != word and sorted(candidate.lower()) == sorted(word):
            expected.append(candidate)

    return expected
