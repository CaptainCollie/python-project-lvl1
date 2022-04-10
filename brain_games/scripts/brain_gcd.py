from brain_games.engine import start_game
from brain_games.games.brain_gcd import brain_gcd


def main():
    description = 'Find the greatest common divisor of given numbers.'
    start_game(brain_gcd, description)
