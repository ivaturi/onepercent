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
    l = len(seq)
    return seq[-tail_length:] if tail_length < l else seq


tail = tail_mine