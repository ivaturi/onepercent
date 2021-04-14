#! /usr/bin/env python

from collections import Counter as ctr
def count_words(sentence):
    return dict(ctr(sentence.lower().split()))