#! /usr/bin/env python

from collections import Counter
import re

def count_words(sentence):
    cleaned = re.findall(r"\b[\w'-]+\b", sentence.lower())
    return dict(Counter(cleaned))