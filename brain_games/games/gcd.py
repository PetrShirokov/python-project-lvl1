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


def gen_game_data():
    NUM1_RANGE = (1, 99)
    NUM2_RANGE = (1, 99)
    num1 = randint(NUM1_RANGE[0], NUM1_RANGE[1])
    num2 = randint(NUM2_RANGE[0], NUM2_RANGE[1])
    question_content = '{} {}'.format(num1, num2)
    right_answer = str(find_gcd(num1, num2))
    return question_content, right_answer
