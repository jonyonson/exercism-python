def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in sentence.lower():
        alphabet = alphabet.replace(char, "")

    return bool(not alphabet)
