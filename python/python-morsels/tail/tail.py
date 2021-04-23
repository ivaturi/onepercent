#! /usr/bin/env python


"""
This solution works, but is sub-optimal, since it involves converting the entire
generator in one go to a list. This fails hard if the input sequence is a 50gb file
because it'll eat up memory
"""
def tail_mine(sequence, tail_length):
    """ Return last n elements from the input sequence """
    if tail_length <= 0:
        return []
    seq = list(sequence)
    return seq[-tail_length:] if tail_length < len(seq) else seq


def tail_trey1(s, n):
    """ Store the last n times we've seen """
    out = []
    if n <= 0:  # edge case
        return  []
    for i in s:
        if n == 1:   # edge case
            out = [i]
        else:
            out = [*out[-(n-1):], i]
    return out


tail = tail_trey1