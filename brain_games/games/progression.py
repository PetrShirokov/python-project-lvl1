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
    INITIAL_TERM = randint(1, 20)
    COMMON_DIFF = randint(1, 10)
    LENGTH = randint(5, 10)
    progression = build_progression(INITIAL_TERM, COMMON_DIFF, LENGTH)
    INDEX_HIDDEN_TERM = randint(0, LENGTH - 1)
    right_answer = str(progression[INDEX_HIDDEN_TERM])
    question_content = progression_to_str(progression, INDEX_HIDDEN_TERM)
    return question_content, right_answer
