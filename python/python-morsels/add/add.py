#! /usr/bin/env python

def add(*args):
    _check_shapes(args, who="trey")
    return [
        [sum(i) for i in zip(*k)] for k in zip(*args)
    ]

def _check_shapes(args, who="me"):
    if who == "me":
        zipped_lengths =  list(map(lambda mi : list(map(len, mi)), zip(*args)))
        if len(set(list(map(len, args)))) > 1 or len(set(list(map(lambda x: len(set(x)) == 1, zipped_lengths)))) != 1:
            raise ValueError("Value error!")
    else:
        matrix_shapes = {
            tuple(len(m) for m in matrix) for matrix in args
        }
        if len(matrix_shapes) > 1:
            raise ValueError("Inputs aren't the same shape!")