"""GCD game."""
# !/usr/bin/env python
import random

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def is_prime(n):
    """Check number if it's prime."""
    if n == 1:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return True if d * d > n else False


def game():
    rand_n = random.randint(1, 100)
    correct = 'yes' if is_prime(rand_n) else 'no'
    return [rand_n], correct
