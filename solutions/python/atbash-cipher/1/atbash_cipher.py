def encode(plain_text):
    result = []

    for char in plain_text.lower():
        if char.isalpha():
            result.append(chr(ord('z') - (ord(char) - ord('a'))))

        elif char.isdigit():
            result.append(char)

    encoded = ''.join(result)

    # Group into chunks of 5 characters
    return ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(ciphered_text):
    result = []

    for char in ciphered_text:
        if char.isalpha():
            result.append(chr(ord('z') - (ord(char) - ord('a'))))

        elif char.isdigit():
            result.append(char)

    return ''.join(result)