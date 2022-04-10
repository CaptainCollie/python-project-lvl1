"""Calculator game."""
# !/usr/bin/env python
import random


def calculator_game():
    """Calculator game."""
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    signs_map = {
        '+': rand_num1 + rand_num2,
        '-': rand_num1 - rand_num2,
        '*': rand_num1 * rand_num2
    }
    rand_sign = random.choice(list(signs_map.keys()))
    cor = str(signs_map.get(rand_sign, ''))
    question = [f'{rand_num1} {rand_sign} {rand_num2}']
    return question, cor
