"""GCD game."""
# #!/usr/bin/env python
import random
from brain_games.scripts.brain_games import start_game


def is_prime(n):
    """Check number if it's prime."""
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return True if d * d > n else False


def prime_game():
    rand_n = random.randint(1, 100)
    cor = 'yes' if is_prime(rand_n) else 'no'
    print(f'Question: {rand_n}')
    answer = input('Your answer: ')
    return answer, cor


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501
    start_game(prime_game, description)


if __name__ == '__main__':
    main()
