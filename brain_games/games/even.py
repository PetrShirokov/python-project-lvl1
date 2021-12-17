from random import randint

TASK_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    result = True if ((number % 2) == 0) else False
    return result


def gen_game_data():
    random_number = randint(1, 99)
    question_content = str(random_number)
    right_answer = 'yes' if is_even(random_number) else 'no'
    game_data_list = [question_content, right_answer]
    return game_data_list
