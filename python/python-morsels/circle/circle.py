#! /usr/bin/env python
from math import pi

class Circle:

    def __init__(self, radius = 1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, val):
      if val < 0:
        raise ValueError("radius cannot be negative")
      self._radius = val
      self._diameter = 2 * self._radius
      self._area = pi * self._radius * self._radius
    
    @property
    def diameter(self):
      return self._diameter
    @diameter.setter
    def diameter(self, val):
        self.radius = 0.5 * val

    @property
    def area(self):
      return self._area