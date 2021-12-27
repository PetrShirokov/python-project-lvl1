from random import randint

TASK_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def gen_game_data():
    NUM_LOWER_BOUND = 1
    NUM_UPPER_BOUND = 99
    num_for_question = randint(NUM_LOWER_BOUND, NUM_UPPER_BOUND)
    question_content = str(num_for_question)
    right_answer = 'yes' if is_even(num_for_question) else 'no'
    return question_content, right_answer
