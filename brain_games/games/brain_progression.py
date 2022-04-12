"""Progression game."""
# !/usr/bin/env python
import random

description = 'What number is missing in the progression?'


def game():
    """Progression game."""
    unkwn = '..'
    rand_start = random.randint(1, 30)
    rand_step = random.randint(2, 10)
    finish = rand_start + 1 + rand_step * 10
    rand_el = random.randint(0, 9)
    generated_progression = list(range(rand_start, finish, rand_step))
    unknown_element = generated_progression[rand_el]
    question = [i if i != unknown_element else unkwn for i in generated_progression]
    correct = str(generated_progression[rand_el])
    return question, correct
