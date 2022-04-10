from brain_games.engine import start_game
from brain_games.games.brain_prime import prime_game


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501
    start_game(prime_game, description)
