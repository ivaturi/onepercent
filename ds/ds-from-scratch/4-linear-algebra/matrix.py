#! /usr/bin/env python

from typing import List
from typing import Tuple
from typing import Callable

# A matrix is a second-order list of floats
Vector = List[float]
Matrix = List[List[float]]

def shape(m: Matrix) -> Tuple[int, int]:
    x = len(m)
    y = len(m[0]) if m else 0
    return x,y

def get_row(m: Matrix, row_index: int) -> Vector:
    try:
        return m[row_index]
    except:
        return False

def get_col(m: Matrix, col_index: int) -> Vector:
    try:
        return [row[col_index] for row in m]
    except:
        return False

def make_matrix(rows: int, cols: int, fn : Callable[[int, int], float]) -> Matrix:
    return [[fn(i,j) for j in range(cols)] for i in range(rows)]

def identity_matrix(size : int) -> Matrix:
    return make_matrix(size, size, lambda i, j: 1 if i==j else 0)


if __name__ == "__main__":
    m1 = [[1,2]]
    m2 = [[1,2,3],[4,5,6]]
    print(shape(m1))
    print(shape(m2))
    print(get_row(m1, 1))
    print(get_row(m2, 1))
    print(get_col(m1, 3))
    print(get_col(m2, 2))
    print(identity_matrix(5))
