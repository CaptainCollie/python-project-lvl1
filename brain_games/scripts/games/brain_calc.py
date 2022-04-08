"""Calculator game."""
# #!/usr/bin/env python
import random


def calculator_game():
    """Calculator game."""
    signs = ['+', '-', '*']
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    rand_sign = random.choice(signs)
    print(f'Question: {rand_num1} {rand_sign} {rand_num2}')
    answer = int(input('Your answer: '))
    if rand_sign == '+':
        cor = rand_num1 + rand_num2
    elif rand_sign == '-':
        cor = rand_num1 - rand_num2
    else:
        cor = rand_num1 * rand_num2
    return answer, cor
