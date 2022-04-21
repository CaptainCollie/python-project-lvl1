"""GCD game."""
import random

DESCRIPTION = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def is_prime(n):
    """Check number if it's prime."""
    if n == 1:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def get_question_and_correct_answer():
    rand_n = random.randint(1, 100)
    correct = 'yes' if is_prime(rand_n) else 'no'
    question = str(rand_n)
    return question, correct
