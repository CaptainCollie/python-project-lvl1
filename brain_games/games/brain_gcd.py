"""GCD game."""
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Find GCD."""
    if a == b:
        return a
    return gcd(a - b, b) if a > b else gcd(a, b - a)


def get_question_and_correct_answer():
    """GCD game."""
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    correct = str(gcd(rand1, rand2))
    question = f'{rand1} {rand2}'
    return question, correct
