"""Progression game."""
#!/usr/bin/env python
import random                                                                                                                            
from ..cli import welcome_user


def progression_game():
    """Progression game."""
    name = welcome_user()

    print('What number is missing in the progression?')
    flag = 1
    unkwn = '..'
    for _ in range(3):
        rand_start = random.randint(1, 30)
        rand_step = random.randint(2, 10)
        finish = rand_start + 1 + rand_step * 10
        rand_el = random.randint(0, 9)
        
        list_gen = list(range(rand_start, finish, rand_step))
        unkwn_el = list_gen[rand_el]
        print(f'Question: ', *[i if i != unkwn_el else unkwn for i in list_gen])
        answer = int(input('Your answer: '))

        if answer == list_gen[rand_el]:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{list_gen[rand_el]}'.")
            print(f"Let's try again, {name}!")
            flag = 0
            break
    
    if flag:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    progression_game()
