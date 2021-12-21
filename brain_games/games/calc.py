from random import randint, choice

TASK_MESSAGE = 'What is the result of the expression?'


def gen_game_data():
    num1 = randint(11, 20)
    num2 = randint(1, 10)
    # list of tuples (question_content_str, right_answer_str)
    game_data = [("{} + {}".format(num1, num2), str(num1 + num2)),
                 ("{} - {}".format(num1, num2), str(num1 - num2)),
                 ("{} * {}".format(num1, num2), str(num1 * num2))]
    return choice(game_data)
