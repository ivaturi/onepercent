from collections import Counter
import re

def count_words(phrase):
    valid_words = r"([a-z0-9A-Z]+(?:['][a-z0-9A-Z]+)?)"
    return Counter(re.findall(valid_words, phrase.lower()))