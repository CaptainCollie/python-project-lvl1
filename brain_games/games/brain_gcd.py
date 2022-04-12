"""GCD game."""
# !/usr/bin/env python
import random

description = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Find GCD."""
    if a == b:
        return a
    return gcd(a - b, b) if a > b else gcd(a, b - a)


def game():
    """GCD game."""
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    correct = str(gcd(rand1, rand2))
    return [rand1, rand2], correct
