from brain_games.engine import start_game
from brain_games.games.brain_even import brain_even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    start_game(brain_even, description)
