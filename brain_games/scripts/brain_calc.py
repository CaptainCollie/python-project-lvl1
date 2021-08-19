"""Calculator game."""
#!/usr/bin/env python
import random


def calculator_game():
    """Calculator game."""
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ').capitalize()
    print(f'Hello, {name}!')

    signs = ['+', '-', '*']

    print('What is the result of the expression?')
    flag = 1
    for _ in range(3):
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        rand_sign = random.choice(signs)
        print(f'Question: {rand_num1} {rand_sign} {rand_num2}')
        answer = int(input('Your answer: '))
        if rand_sign == '+':
            correct = rand_num1 + rand_num2
        elif rand_sign == '-':
            correct = rand_num1 - rand_num2
        else:
            correct = rand_num1 * rand_num2
        
        if correct == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            flag = 0
            break
    if flag:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    calculator_game()
