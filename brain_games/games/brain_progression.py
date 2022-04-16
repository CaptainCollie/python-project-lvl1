"""Progression game."""
# !/usr/bin/env python
import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    """Progression game."""
    rand_start = random.randint(1, 30)
    rand_step = random.randint(2, 10)
    progression_length = random.randint(5, 10)
    finish = rand_start + 1 + rand_step * progression_length
    rand_el = random.randint(0, progression_length - 1)
    generated_progression = list(range(rand_start, finish, rand_step))
    unknown_element = generated_progression[rand_el]
    question = ' '.join([str(i) if i != unknown_element else '..'
                         for i in generated_progression])
    correct = str(generated_progression[rand_el])
    return question, correct
