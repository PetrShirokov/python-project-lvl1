from random import randint, shuffle

TASK_MESSAGE = 'What is the result of the expression?'


def make_calc_operation():
    """Returns one random math operation from
    the list: ['+', '-' and '*']."""
    operation_list = list(['sum', 'sub', 'mul'])
    shuffle(operation_list)
    calc_operation = operation_list[0]
    return calc_operation


def calc_operation_res(operation, num1, num2):
    if operation == 'sum':
        return (num1 + num2)
    elif operation == 'sub':
        return abs(num2 - num1)
    elif operation == 'mul':
        return (num1 * num2)


def make_task_txt(operation, num1, num2):
    if operation == 'sum':
        text = ('{} + {}').format(num1, num2)
    elif operation == 'sub':
        max_num = max(num1, num2)
        min_num = min(num1, num2)
        text = ('{} - {}').format(max_num, min_num)
    elif operation == 'mul':
        text = ('{} * {}').format(num1, num2)
    return text


def gen_game_data():
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    current_operation = make_calc_operation()
    operation_result = calc_operation_res(current_operation, num1, num2)
    question_content = make_task_txt(current_operation, num1, num2)
    right_answer = str(operation_result)
    return (question_content, right_answer)
