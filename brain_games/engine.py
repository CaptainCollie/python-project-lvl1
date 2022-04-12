from brain_games.cli import welcome_user


def start_game(game):
    name = welcome_user()
    print(game.description)
    for _ in range(3):
        question, correct = game.game()
        print('Question:', *question)
        answer = input('Your answer: ').lower()
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
    else:
        print(f'Congratulations, {name}!')
