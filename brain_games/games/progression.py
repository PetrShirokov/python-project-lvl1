import prompt
from random import randint
from brain_games.cli import print_message, bye_user


def progression():
    """Builds arithmetic progression with random lenght
    (from 5 to 10 members) and random step (from 1 to 10).
    One of the members is hidden by two dots.
    Returns progression(string)."""

    a0 = randint(1, 30)
    d = randint(1, 10)
    k_max = randint(4, 9)
    k_mystery = randint(1, k_max)
    k = 0
    progression_str = ' '
    global hidden_member
    hidden_member = a0 + (k_mystery * d)
    while k <= k_max:
        a = str(a0 + (k * d)) if k != k_mystery else '..'
        progression_str += str(a) + '  '
        k = k + 1
    return progression_str


def game_progression():
    progression()
    print('What number is missing in the progression?')
    k = 0
    while k < 3:
        question = 'Question: {}'.format(progression())
        print(question)
        answer = prompt.string('Your answer: ')
        right_answer = str(hidden_member)
        print_message(answer, right_answer)
        if answer == right_answer:
            k = k + 1
        else:
            k = 666
    if k == 3:
        bye_user()
