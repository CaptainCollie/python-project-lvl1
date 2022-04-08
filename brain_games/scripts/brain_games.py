"""Brain games executable file."""
# #!/usr/bin/env python
from ..cli import welcome_user

from brain_games.scripts.games.brain_calc import calculator_game
from brain_games.scripts.games.brain_even import brain_even
from brain_games.scripts.games.brain_gcd import brain_gcd
from brain_games.scripts.games.brain_prime import prime_game
from brain_games.scripts.games.brain_progression import progression_game


def main():
    """Brain games welcome function."""
    return welcome_user()


def start_brain_progression():
    description = 'What number is missing in the progression?'
    start_game(progression_game, description)


def start_brain_prime():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501
    start_game(prime_game, description)


def start_brain_gcd():
    description = 'Find the greatest common divisor of given numbers.'
    start_game(brain_gcd, description)


def start_brain_calc():
    description = 'What is the result of the expression?'
    start_game(calculator_game, description)


def start_brain_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(brain_even, description)


def start_game(game, game_description):
    name = main()
    print(game_description)
    for _ in range(3):
        answer, correct = game()
        if not check_answer(name, answer, correct):
            break
    else:
        print(f'Congratulations, {name}!')


def check_answer(name, answer, correct):
    if answer == correct:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False
