from random import randint

TASK_MESSAGE = 'What number is missing in the progression?'


def gen_progression_with_hidden_member():
    """Builds arithmetic progression with random lenght
    (from 5 to 10 members) and random step (from 1 to 10).
    One of the members is hidden by two dots."""
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
    return progression_str


def gen_game_data(number_of_questions: int):
    """Returns 2 lists with the equal lenghts
    len(list1) = len(list2) = number_of_questions.
    First list contains questions for the game.
    Second contains right answers on the same positions."""
    questions_list = list()
    right_answers_list = list()
    for questions_count in range(0, number_of_questions):
        question_content = gen_progression_with_hidden_member()
        question = 'Question: {}'.format(question_content)
        questions_list.append(question)
        right_answer = hidden_member
        right_answers_list.append(right_answer)
    return questions_list, right_answers_list
