from brain_games.engine import start_game
from brain_games.games.brain_calc import calculator_game


def main():
    description = 'What is the result of the expression?'
    start_game(calculator_game, description)
