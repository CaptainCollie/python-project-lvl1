#!/usr/bin/env python   
"""The game."""
import random
from ..cli import welcome_user


def game():
    """The game function."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    flag = 1
    for _ in range(3):
        random_number = random.randint(1, 1000)
        print(f'Question: {random_number}')
        answer = input('Your answer: ').lower()
        if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 == 1 and answer == 'no'):
            print('Correct')
        else:
            flag = 0
            if answer == 'yes':
                correct = 'no'
            else:
                correct = 'yes'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'")
            print(f"Let's try again, {name}!")
            break
    if flag:
        print(f'Congratulations, {name}!')


if __name__ == '__game__':
    game()
