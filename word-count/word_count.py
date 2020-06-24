import re


def count_words(sentence):
    sentence = sentence.replace('_', ' ')
    words = re.findall(r'\w+\'s|\w+\'t|\w+\'re|\w+', sentence.lower())

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
