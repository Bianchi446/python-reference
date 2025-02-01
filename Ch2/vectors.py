""" 
    Vector class implementation using the special methods __repr__, __abs__, __add__, __mull__, __bool__
"""

import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)  # Returns the magnitude of the vector

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __bool__(self):
        return (self.x or self.y)  # Returns False if the vector is (0, 0), True otherwise

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)  # Corrected method name




v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)         # Vector(4, 6)
print(abs(v1))         # 5.0 (magnitude of the vector)
print(v1 * 2)          # Vector(6, 8)
print(bool(Vector(0, 0)))  # False
print(bool(v1))        # True

