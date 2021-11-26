from random import randint


def gen_progression_with_hidden_member():
    """Builds arithmetic progression with random lenght
    (from 5 to 10 members) and random step (from 1 to 10).
    One of the members is hidden by two dots.
    Returns list [progression_str, hidden_member_str]."""
    a0 = randint(1, 30)
    d = randint(1, 10)
    k_max = randint(4, 9)  # upper index of brain progression
    k_mystery = randint(0, k_max)  # index of hidden progression's member
    k = 0
    progression_str = ''
    global hidden_member
    hidden_member = a0 + (k_mystery * d)
    while k <= k_max:
        a = str(a0 + (k * d)) if k != k_mystery else '..'
        progression_str += str(a) + ' '
        k = k + 1
    progression_with_hidden_member = [progression_str, str(hidden_member)]
    return progression_with_hidden_member
