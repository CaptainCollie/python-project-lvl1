from brain_games.cli import welcome_user


def start_game(game, game_description):
    name = welcome_user()
    print(game_description)
    for _ in range(3):
        question, correct = game()
        print('Question:', *question)
        answer = int(input('Your answer: '))
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
