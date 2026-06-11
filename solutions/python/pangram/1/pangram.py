def is_pangram(sentence):
    sentence_1=sentence.lower().strip()
    for item in range(97,123):
        if chr(item) not in sentence_1:
           return False
    return True