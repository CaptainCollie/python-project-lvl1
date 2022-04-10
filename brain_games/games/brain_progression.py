"""Progression game."""
# !/usr/bin/env python
import random


def progression_game():
    """Progression game."""
    unkwn = '..'
    rand_start = random.randint(1, 30)
    rand_step = random.randint(2, 10)
    finish = rand_start + 1 + rand_step * 10
    rand_el = random.randint(0, 9)
    list_gen = list(range(rand_start, finish, rand_step))
    unkwn_el = list_gen[rand_el]
    question = [i if i != unkwn_el else unkwn for i in list_gen]
    cor = list_gen[rand_el]
    return question, cor
