"""Calculator game."""
# #!/usr/bin/env python
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
    print(f'Question: {rand_num1} {rand_sign} {rand_num2}')
    answer = int(input('Your answer: '))
    cor = signs_map.get(rand_sign, '')
    return answer, cor
