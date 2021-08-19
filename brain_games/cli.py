"""Welcome user."""
import prompt


def welcome_user():
    """Welcome user function."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name.capitalize()}')


if __name__ == '__main__':
    welcome_user()
