#! /usr/bin/env python

from math import sqrt, pi, exp, erf
from collections import Counter
import random
import matplotlib.pyplot as plt

# uniform probability density
def pdf_uniform(x):
    return 1 if 0 <= x < 1 else 0

# uniform cumulative density
def cdf_uniform(x):
    if x < 0:
        return 0
    if x > 1:
        return 1
    return x

# normal probability density
def pdf_normal(x, mu, sigma):
    c = 1  / (sqrt(2 * pi) * sigma)
    e = exp( - (x - mu)**2 / (2 * sigma**2))
    return c * e

# normal cdf
def cdf_normal(x, mu, sigma):
    return (1 + erf( (x - mu) / sqrt(2) / sigma)) /2

# inverse of the normal cdf (to find a value corresponding to a specific probability)
# (uses binary search)
def cdf_inverse_normal(p, mu = 0, sigma = 1, tol = 0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * cdf_normal_inverse(p, tol = tol)
    low = -10
    high = 10
    while high - low > tol:
        x = (low + high)/2
        px = cdf_normal(x, mu, sigma)
        if px < p:
            low = x
        else:
            high = x
    return x


# bernoulli trials: return 1 with probability p
def bernoulli(p):
    return 1 if random.random() < p else 0

# the sum of n bernoulli trials, each trial returning 1 with probability p
def binomial(n, p):
    return sum([bernoulli(p) for _ in range(n)])

def binomial_histogram(n, p, n_pts):
    
    # data from n throws 
    data = [binomial(n, p) for _ in range(n_pts)]

    h = Counter(data)
    plt.bar([x - 0.4 for x in h.keys()],
            [v/n_pts for v in h.values()],
            0.8)
    
    # mean and std. dev. for a bernoulli distribution
    # according to the central limit theorem
    mu = n * p
    sigma = sqrt(n * p * (1 - p))

    xs = range(min(data), max(data) + 1)
    ys = [cdf_normal(i + 0.5, mu, sigma) - cdf_normal(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial distribution vs normal approximation")
    plt.show()


