#! /usr/bin/env python
from math import sqrt
from lib import vector

def median(arr):
    """Compute the midpoint of the data"""
    if len(arr) % 2:
        return sorted(arr)[len(arr) // 2]
    else:
        midpoint = len(arr)//2
        return 0.5 * (sorted(arr)[midpoint - 1] + sorted(arr)[midpoint + 1])

def quantile(arr, nth):
    """compute the value under which the nth percentile of the (sorted) data lies"""
    nth_index = int( nth * len(arr))
    return arr[nth_index]

def range(arr):
    """Compute the range of the input data"""
    sorted_arr = sorted(arr)
    return abs(sorted_arr[-1] - sorted_arr[0])

def mean(arr):
    return sum(arr)/len(arr)

def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]

def variance(arr):
    # Translate the mean to 0 and compute the sum of squares
    n = len(arr)
    distances = de_mean(arr)
    return sum([i**2 for i in distances])/(n-1)

def std_dev(arr):
    return sqrt(variance(arr))

def de_mean(arr):
    avg = mean(arr)
    return [x - avg for x in arr]

def interquantile_range(arr):
    return abs(quantile(arr, 0.75) - quantile(arr, 0.25))

def covariance(v1, v2):
    assert len(v1) == len(v2), "Input vectors must be of the same length!"
    return vector.dot(de_mean(v1), de_mean(v2)) / (len(v1) - 1)

def correlation(v1, v2):
    v1s = std_dev(v1)
    v2s = std_dev(v2)
    return covariance(v1, v2)/v1s/v2s if v1s > 0 and v2s > 0 else 0
        
if __name__ == "__main__":

    from collections import Counter
    from matplotlib import pyplot as plt


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

    num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    #fcounthist(num_friends)
    friendstats(num_friends)