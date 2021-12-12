from random import randint

TASK_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int):
    """Return 'yes' if num is prime, and 'no' if it's not.
    Num is natural and greater or equal two."""
    if num == 2:
        is_prime_str = 'yes'
    upper_range_bound = (num // 2) + 1
    for i in range(2, upper_range_bound):
        expected_divisor = num // i
        if num % expected_divisor == 0:
            is_prime_str = 'no'
            return is_prime_str
    is_prime_str = 'yes'
    return is_prime_str


def gen_game_data(number_of_questions: int):
    """Returns 2 lists with the equal lenghts
    len(list1) = len(list2) = number_of_questions.
    First list contains questions for the game.
    Second contains right answers on the same positions."""
    questions_list = list()
    right_answers_list = list()
    for questions_count in range(0, number_of_questions):
        random_number = randint(2, 99)
        question = 'Question: {}'.format(str(random_number))
        questions_list.append(question)
        right_answer = is_prime(random_number)
        right_answers_list.append(right_answer)
    return questions_list, right_answers_list
