"""The game that ask you to asnwer if number is even or not"""
# #!/usr/bin/env python
import random


def brain_even():
    """The game function."""
    random_number = random.randint(1, 1000)
    print(f'Question: {random_number}')
    answer = input('Your answer: ').lower()
    cor = 'yes' if is_even(random_number) else 'no'
    return answer, cor


def is_even(n):
    return n % 2 == 0
