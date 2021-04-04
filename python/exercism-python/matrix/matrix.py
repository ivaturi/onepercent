#! /usr/bin/env python
class Matrix:
    def __init__(self, matrix_string):
       
        # can this be simplified?
        self.rows = [list(map(int, s.split(" "))) for s in matrix_string.split("\n")]
        
        # list(zip) doesn't work because it outputs sets, and we're expecting arrays
        self.cols = list(map(list,zip(*self.rows)))

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.cols[index-1]

