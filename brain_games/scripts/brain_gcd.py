"""GCD game."""
#!/usr/bin/env python
import random
from ..cli import welcome_user


def gcd(a, b):
    """Find GCD."""
    if a == b:
        return a
    return gcd(a - b, b) if a > b else gcd(a, b - a)


def brain_gcd():
    """GCD game."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    
    flag = 1
    for _ in range(3):
        rand1 = random.randint(1, 100)
        rand2 = random.randint(1, 100)

        print(f'Question: {rand1} {rand2}')
        answer = int(input('Your answer: '))
        correct = gcd(rand1, rand2)
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            flag = 0
            break
    if flag:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    brain_gcd()
