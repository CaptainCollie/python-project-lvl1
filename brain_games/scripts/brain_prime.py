"""GCD game."""
# #!/usr/bin/env python
import random
from ..cli import welcome_user


def is_prime(n):
    """Check number if it's prime."""
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return True if d * d > n else False


def prime_game():
    name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    flag = 1
    for _ in range(3):
        rand_n = random.randint(1, 100)
        cor = 'yes' if is_prime(rand_n) else 'no'
        print(f'Question: {rand_n}')
        answer = input('Your answer: ')

        if answer == cor:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            flag = 0
            break
    if flag:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    prime_game()
