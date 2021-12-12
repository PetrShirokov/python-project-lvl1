from random import randint

TASK_MESSAGE = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    """Returns the greatest common divisor of
    two positive (> 0) integer numbers."""
    min_common_divisor = 1
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    if max_num % min_num == 0:
        return min_num
    supposed_result_of_division = 2
    max_result_of_division = min_num // 2
    while supposed_result_of_division <= max_result_of_division:
        divisor = min_num // supposed_result_of_division
        if (max_num % divisor == 0) and (min_num % divisor == 0):
            return divisor
        supposed_result_of_division += 1
    return min_common_divisor


def gen_game_data(number_of_questions: int):
    """Returns 2 lists with the equal lenghts
    len(list1) = len(list2) = number_of_questions.
    First list contains questions for the game.
    Second contains right answers on the same positions."""
    questions_list = list()
    right_answers_list = list()
    for questions_count in range(0, number_of_questions):
        random_number1 = randint(1, 99)
        random_number2 = randint(1, 99)
        question = 'Question: {} {}'.format(random_number1, random_number2)
        questions_list.append(question)
        right_answer = find_gcd(random_number1, random_number2)
        right_answers_list.append(right_answer)
    return questions_list, right_answers_list
