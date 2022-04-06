"""Brain games executable file."""
# #!/usr/bin/env python
from ..cli import welcome_user


def main():
    """Brain games welcome function."""
    return welcome_user()


def start_game(game, game_description):
    name = main()
    print(game_description)
    for _ in range(3):
        answer, correct = game()
        if not check_answer(name, answer, correct):
            break
    else:
        print(f'Congratulations, {name}!')


def check_answer(name, answer, correct):
    if answer == correct:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False


if __name__ == '__main__':
    main()
