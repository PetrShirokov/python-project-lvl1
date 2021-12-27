from random import randint, choice

TASK_MESSAGE = 'What is the result of the expression?'


def gen_game_data():
    NUM1_RANGE = (11, 20)
    NUM2_RANGE = (1, 10)
    num1 = randint(NUM1_RANGE[0], NUM1_RANGE[1])
    num2 = randint(NUM2_RANGE[0], NUM2_RANGE[1])
    # list of tuples (question_content_str, right_answer_str)
    game_data = [("{} + {}".format(num1, num2), str(num1 + num2)),
                 ("{} - {}".format(num1, num2), str(num1 - num2)),
                 ("{} * {}".format(num1, num2), str(num1 * num2))]
    return choice(game_data)
