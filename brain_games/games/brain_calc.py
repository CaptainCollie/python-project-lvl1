"""Calculator game."""
# !/usr/bin/env python
import random

DESCRIPTION = 'What is the result of the expression?'


def run():
    """Calculator game."""
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    signs_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    rand_sign = random.choice(list(signs_map.keys()))
    correct = str(signs_map.get(rand_sign)(rand_num1, rand_num2))
    question = f'{rand_num1} {rand_sign} {rand_num2}'
    return question, correct
