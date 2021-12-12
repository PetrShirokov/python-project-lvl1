from random import randint

TASK_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """Returns 'yes' if number is even, else 'no'."""
    answer = 'yes' if (number % 2) == 0 else 'no'
    return answer


def gen_game_data(number_of_questions: int):
    """Returns 2 lists with the equal lenghts
    len(list1) = len(list2) = number_of_questions.
    First list contains questions for the game.
    Second contains right answers on the same positions."""
    questions_list = list()
    right_answers_list = list()
    for questions_count in range(0, number_of_questions):
        random_number = randint(1, 99)
        question = 'Question: {}'.format(str(random_number))
        questions_list.append(question)
        right_answer = is_even(random_number)
        right_answers_list.append(right_answer)
    return questions_list, right_answers_list
