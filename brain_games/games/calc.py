from random import shuffle


def choose_operation_for_calc():
    """Choose operation for game-calc from '+', '-' and '*'."""
    operation_lst = list(['sum', 'sub', 'mul'])
    shuffle(operation_lst)
    current_operation = operation_lst[0]
    return current_operation


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
