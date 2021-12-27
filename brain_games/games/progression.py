from random import randint

TASK_MESSAGE = 'What number is missing in the progression?'


def build_progression(initial_term, common_diff, length):
    finite_term = initial_term + (length - 1) * common_diff
    progression = list(range(initial_term, finite_term + 1, common_diff))
    return progression


def progression_to_str(progression, index_hidden_term):
    for n in range(0, len(progression)):
        progression[n] = str(progression[n])
    progression[index_hidden_term] = '..'
    return " ".join(progression)


def gen_game_data():
    INITIAL_TERM_RANGE = (1, 20)
    COM_DIFF_RANGE = (1, 10)
    MIN_LENGTH = 5
    MAX_LENGTH = 10
    initial_term = randint(INITIAL_TERM_RANGE[0], INITIAL_TERM_RANGE[1])
    common_diff = randint(COM_DIFF_RANGE[0], COM_DIFF_RANGE[1])
    length = randint(MIN_LENGTH, MAX_LENGTH)
    progression = build_progression(initial_term, common_diff, length)
    index_hidden_term = randint(0, length - 1)
    right_answer = str(progression[index_hidden_term])
    question_content = progression_to_str(progression, index_hidden_term)
    return question_content, right_answer
