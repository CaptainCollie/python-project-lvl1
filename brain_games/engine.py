from brain_games.cli import welcome_user


def start_game(game, n=3):
    name = welcome_user()
    print(game.DESCRIPTION)
    for _ in range(n):
        question, correct = game.run()
        print('Question:', question)
        answer = input('Your answer: ').lower()
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
    else:
        print(f'Congratulations, {name}!')
