from random import randint

TASK_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int):
    """Returns True if num is prime, and False if it's not.
    Num is natural and greater or equal two."""
    if num == 2:
        return True
    upper_range_bound = (num // 2) + 1
    for i in range(2, upper_range_bound):
        expected_divisor = num // i
        if num % expected_divisor == 0:
            return False
    return True


def gen_game_data():
    NUM_LOWER_BOUND = 2
    NUM_UPPER_BOUND = 99
    num_for_question = randint(NUM_LOWER_BOUND, NUM_UPPER_BOUND)
    question_content = str(num_for_question)
    right_answer = 'yes' if is_prime(num_for_question) else 'no'
    return question_content, right_answer
