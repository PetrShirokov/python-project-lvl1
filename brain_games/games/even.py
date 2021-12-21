from random import randint

TASK_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return (number % 2 == 0)


def gen_game_data():
    random_number = randint(1, 99)
    question_content = str(random_number)
    right_answer = 'yes' if is_even(random_number) else 'no'
    return (question_content, right_answer)
