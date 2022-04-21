"""Calculator game."""
import random

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_correct_answer():
    """Calculator game."""
    rand_num1 = random.randint(1, 100)
    rand_num2 = random.randint(1, 100)
    operators_map = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
    rand_sign = random.choice(list(operators_map.keys()))
    func = operators_map.get(rand_sign)
    correct = str(func(rand_num1, rand_num2))
    question = f'{rand_num1} {rand_sign} {rand_num2}'
    return question, correct
