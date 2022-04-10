"""GCD game."""
# !/usr/bin/env python
import random


def gcd(a, b):
    """Find GCD."""
    if a == b:
        return a
    return gcd(a - b, b) if a > b else gcd(a, b - a)


def brain_gcd():
    """GCD game."""
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    cor = str(gcd(rand1, rand2))
    return [rand1, rand2], cor
