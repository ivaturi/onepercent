#! /usr/bin/env python
import random

def shape(matrix):
    x = len(matrix)
    y = len(matrix[0]) if matrix else 0
    return x,y

def get_row(matrix, row_idx):
    try:
        return matrix[row_idx]
    except:
        return False

def get_col(matrix, col_idx):
    try:
        return [row[col_idx] for row in matrix]
    except:
        return False

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def create_from_function(dims, function):
    rows, cols = dims[0], dims[1]
    return [[function(i,j) for j in range(cols)] for i in range(rows)]

def create_identity(size):
    return create_from_function([size, size], lambda i, j: 1 if i==j else 0)

def create_random(*dims):
    if len(dims) == 1:
        rows = cols = dims[0]
    else:
        rows = dims[0]
        cols = dims[1]
    return create_from_function([rows, cols], lambda i,j: int(100*random.random()))