import prompt

GAME_ROUNDS_COUNT = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}')
    print(game.DESCRIPTION)
    for _ in range(GAME_ROUNDS_COUNT):
        question, correct = game.get_question_and_correct_answer()
        print('Question:', question)
        answer = input('Your answer: ').lower()
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
