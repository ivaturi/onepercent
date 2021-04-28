#! /usr/bin/env python
import random

def _check(vectors):
  assert len(vectors) > 1, "Need at least two vectors!"
  assert all(len(vec) == len(vectors[0]) for vec in vectors), "All vectors must be the same size!"

def vecsum(*vectors):
  _check(vectors)
  return [sum(vec[i] for vec in vectors) for i in range(len(vectors[0]))]

def diff(v1, v2):
  assert len(v1) == len(v2), "Vectors must be the same length"
  return [v1_i - v2_i for (v1_i, v2_i) in zip(v1, v2)]

def scale(vec, s):
  return [s * v_i for v_i in vec]

def mean(*vectors):
  _check(vectors)
  n = len(vectors)
  return vector_sum(*[scale(vec, 1/n) for vec in vectors])

def dot(v1, v2):
  _check([v1, v2])
  return sum(v1_i * v2_i for v1_i,v2_i in zip(v1, v2))

def sum_of_squares(v1):
  return dot(v1, v1)

def magnitude(v):
  return pow(sum_of_squares(v), 0.5)

def distance(v1,v2):
  _check([v1, v2])
  return magnitude(diff(v1, v2))

def create_random(length):
  return [int(100 * random.random()) for _ in range(length)]