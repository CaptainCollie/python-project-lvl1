"""GCD game."""
# !/usr/bin/env python
import random


def is_prime(n):
    """Check number if it's prime."""
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return True if d * d > n else False


def prime_game():
    rand_n = random.randint(1, 100)
    cor = 'yes' if is_prime(rand_n) else 'no'
    return [rand_n], cor
