#! /usr/bin/env python

from collections import Counter
from matplotlib import pyplot as plt
from typing import List

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def _median(arr):
    """Compute the midpoint of the data"""
    if len(arr) % 2:
        return sorted(arr)[len(arr) // 2]
    else:
        midpoint = len(arr)//2
        return 0.5 * (sorted(arr)[midpoint - 1] + sorted(arr)[midpoint + 1])

def _quantile(arr: List[float], nth : float) -> float:
    """compute the value under which the nth percentile of the (sorted) data lies"""
    nth_index = int( nth * len(arr))
    return arr[nth_index]

def _range(arr : List[float]) -> float:
    """Compute the range of the input data"""
    sorted_arr = sorted(arr)
    return abs(sorted_arr[-1] - sorted_arr[0])

def _mean(arr : List[float]) -> float:
    return sum(arr)/len(arr)

def _variance(arr : List[float]) -> float:
    """Compute the variance of the data in an array"""

    # Translate the mean to 0 and compute the sum of squares
    mean = _mean(arr)
    zeroed_sum_of_squares = sum([(elem - mean)**2 for elem in arr])
    return zeroed_sum_of_squares/(len(arr) -1)


# plot a histogram of friend counts
def fcounthist(num_friends):
    fcounts = Counter(num_friends)
    x_lim = int(1 + max(num_friends))
    xs = range(x_lim)
    ys = [fcounts[i] for i in xs]
    plt.bar(xs, ys)
    plt.axis([0, x_lim, 0, int(1 + max(ys))])
    plt.show()

def friendstats(nfriends):
    # sort values
    sorted_values = sorted(nfriends)
    print("Max number of friends: {}".format(sorted_values[-1]))
    print("Min number of friends: {}".format(sorted_values[0]))
    print("Average number of friends: {}".format(_mean(num_friends)))
    print("Median number of friends: {}".format(_median(num_friends)))
    print("The range of number of friends is {}".format(_range(num_friends)))
    for i in range(90, 100, 3):
        print("{}th quantile : {}".format(i, _quantile(sorted_values, i/100)))
    print("The variance of the number of friends is {}".format(_variance(num_friends)))
        
if __name__ == "__main__":
    #fcounthist(num_friends)
    friendstats(num_friends)