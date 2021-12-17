from random import randint

TASK_MESSAGE = 'What number is missing in the progression?'


def gen_game_data():
    """Builds arithmetic progression with random lenght
    (from 5 to 10 members) and random step (from 1 to 10).
    One of the members is hidden by two dots.
    Returns list, which contain progression_str and
    hidden member_str."""
    a0 = randint(1, 30)
    d = randint(1, 10)
    k_max = randint(4, 9)  # upper index of brain progression
    k_mystery = randint(0, k_max)  # index of hidden progression's member
    k = 0
    progression_str = ''
    hidden_member = a0 + (k_mystery * d)
    while k <= k_max:
        a = str(a0 + (k * d)) if k != k_mystery else '..'
        progression_str += str(a) + ' '
        k = k + 1
    return (progression_str, str(hidden_member))
