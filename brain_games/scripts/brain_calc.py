"""Calculator game."""
# #!/usr/bin/env python
import random
from ..cli import welcome_user


def calculator_game():
    """Calculator game."""
    name = welcome_user()
    signs = ['+', '-', '*']

    print('What is the result of the expression?')
    flag = 1
    for _ in range(3):
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        rand_sign = random.choice(signs)
        print(f'Question: {rand_num1} {rand_sign} {rand_num2}')
        answer = int(input('Your answer: '))
        if rand_sign == '+':
            corr = rand_num1 + rand_num2
        elif rand_sign == '-':
            corr = rand_num1 - rand_num2
        else:
            corr = rand_num1 * rand_num2
        if corr == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{corr}'.")
            print(f"Let's try again, {name}!")
            flag = 0
            break
    if flag:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    calculator_game()
