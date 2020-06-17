import re

def is_isogram(string):
    s = re.sub(r'[-\s]', '', string.lower())
    return len(set(s)) == len(s)
