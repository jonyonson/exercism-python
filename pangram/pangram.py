def is_pangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for char in sentence.lower():
        if not alphabet:
            return True

        if char in alphabet:
            alphabet.remove(char)

    return bool(not alphabet)
