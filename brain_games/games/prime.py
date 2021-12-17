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
    random_number = randint(2, 99)
    question_content = str(random_number)
    right_answer = 'yes' if is_prime(random_number) else 'no'
    return (question_content, right_answer)
