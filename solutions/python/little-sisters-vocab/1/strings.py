"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
   return 'un' + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]

    words = [prefix]

    for word in vocab_words[1:]:
        words.append(prefix + word)

    return " :: ".join(words)

    



def remove_suffix_ness(word):
    base = word[:-4]

    if base.endswith('i'):
        base = base[:-1] + 'y'

    return base


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """

    sentence=sentence.split()
    return sentence[index].strip('.') + 'en'
