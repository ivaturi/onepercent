#! /usr/bin/env python

from math import sqrt, pi, exp

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