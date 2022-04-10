from brain_games.engine import start_game
from brain_games.games.brain_progression import progression_game


def main():
    description = 'What number is missing in the progression?'
    start_game(progression_game, description)
