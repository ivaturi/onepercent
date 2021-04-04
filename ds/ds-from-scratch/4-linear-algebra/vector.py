#! /usr/bin/env python

from typing import List

# What is a vector?
Vector = List[float]

def _check(vectors):
  """Check if a list has at least 2 vectors, and if all vectors have equal length"""
  assert len(vectors) > 1, "Need at least two vectors!"
  assert all(len(vec) == len(vectors[0]) for vec in vectors), "All vectors must be the same size!"

def vector_sum(*vectors) -> Vector:
  """Compute the sum of an arbitrary number vectors"""
  _check(vectors)
  return [sum(vec[i] for vec in vectors) for i in range(len(vectors[0]))]

def diff(v1: Vector, v2: Vector) -> Vector:
  """Compute the pairwise difference between two vectors"""
  assert len(v1) == len(v2), "Vectors must be the same length"
  return [v1_i - v2_i for (v1_i, v2_i) in zip(v1, v2)]

def scale(v: Vector, s: float) -> Vector:
  """Scale a vector by a specified magnitude"""
  return [s * v_i for v_i in v]

def vector_mean(*vectors) -> Vector:
  """Compute the mean of a number of vectors"""
  _check(vectors)
  n = len(vectors)
  return vector_sum(*[scale(vec, 1/n) for vec in vectors])

def dot(v1: Vector, v2: Vector) -> float:
  """Compute the dot product of two vectors"""
  _check([v1, v2])
  return sum(v1_i * v2_i for v1_i,v2_i in zip(v1, v2))

def sum_of_squares(v1: Vector) -> float:
  return dot(v1, v1)

def magnitude(v: Vector) -> float:
  """Compute the magnitude of a vector"""
  return pow(sum_of_squares(v), 0.5)

def distance(v1: Vector, v2: Vector) -> float:
  """Compute the distance between two vectors"""
  _check([v1, v2])
  return magnitude(diff(v1, v2))


def test()
  v1 = [1, 2, 3]
  v2 = [4, 5, 6]
  print(vector_sum(v1, v2))
  print(diff(v2, v1))
  print(scale(v1, 2))
  print(vector_mean(v1, v2))
  print(dot(v1, v2))
  print(sum_of_squares(v2))
  print(magnitude(v1))
  print(distance(v1, v2))