"""GCD game."""
# #!/usr/bin/env python
import random
from brain_games.scripts.brain_games import start_game


def gcd(a, b):
    """Find GCD."""
    if a == b:
        return a
    return gcd(a - b, b) if a > b else gcd(a, b - a)


def brain_gcd():
    """GCD game."""
    rand1 = random.randint(1, 100)
    rand2 = random.randint(1, 100)
    print(f'Question: {rand1} {rand2}')
    answer = int(input('Your answer: '))
    cor = gcd(rand1, rand2)
    return answer, cor


def main():
    description = 'Find the greatest common divisor of given numbers.'
    start_game(brain_gcd, description)


if __name__ == '__main__':
    main()
