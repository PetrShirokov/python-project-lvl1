from random import randint, choice

TASK_MESSAGE = 'What is the result of the expression?'


def gen_game_data():
    NUM1 = randint(11, 20)
    NUM2 = randint(1, 10)
    # list of tuples (question_content_str, right_answer_str)
    game_data = [("{} + {}".format(NUM1, NUM2), str(NUM1 + NUM2)),
                 ("{} - {}".format(NUM1, NUM2), str(NUM1 - NUM2)),
                 ("{} * {}".format(NUM1, NUM2), str(NUM1 * NUM2))]
    return choice(game_data)
