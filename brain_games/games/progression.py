from random import randint

TASK_MESSAGE = 'What number is missing in the progression?'


def build_progression():
    """Returns list with the terms of increasing arithmetic progression.
    Progression has random length (from 5 to 10 terms) and random
    common difference (from 1 to 10)."""
    a = randint(1, 20)  # initial term
    d = randint(1, 10)  # common difference
    n_max = randint(5, 10)  # length of the progression
    progression = [a]
    for n in range(1, n_max):
        a += d
        progression.append(a)
    return progression


def transform_to_str(seq):
    seq_str = ''
    for n in range(0, len(seq)):
        end = ' '
        if n == len(seq) - 1:
            end = ''
        seq_str += str(seq[n]) + end
    return seq_str


def gen_game_data():
    progression = build_progression()
    index_h = randint(0, len(progression) - 1)  # index of hidden term
    hidden_term, progression[index_h] = progression[index_h], '..'
    question_content = transform_to_str(progression)
    right_answer = str(hidden_term)
    return (question_content, right_answer)
