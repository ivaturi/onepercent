#! /usr/bin/env python

def tail(sequence, tail_length):
    """ Return last n elements from the input sequence """
    if tail_length <= 0:
        return []
    seq = list(sequence)
    l = len(seq)
    return [seq[i] for i in range(l-tail_length, l)] if tail_length < l else seq