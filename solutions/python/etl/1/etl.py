def transform(legacy_data):
    new_dict = {}
    for number, letters in legacy_data.items():
        for letter in letters:
            new_dict[letter.lower()] = number
    return dict(sorted(new_dict.items()))
        
