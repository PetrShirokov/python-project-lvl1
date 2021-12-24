from random import randint

TASK_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def gen_game_data():
    NUM_FOR_QUESTION = randint(1, 99)
    question_content = str(NUM_FOR_QUESTION)
    right_answer = 'yes' if is_even(NUM_FOR_QUESTION) else 'no'
    return question_content, right_answer
