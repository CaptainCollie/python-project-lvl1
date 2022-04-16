"""The game that ask you to asnwer if number is even or not"""
# !/usr/bin/env python
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def get_question_and_correct_answer():
    """The game function."""
    random_number = random.randint(1, 1000)
    correct = 'yes' if is_even(random_number) else 'no'
    question = str(random_number)
    return question, correct
