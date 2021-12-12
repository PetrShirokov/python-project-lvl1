from random import randint, shuffle

TASK_MESSAGE = 'What is the result of the expression?'


def make_operations_list_for_calc():
    """Returns list of math operations: ['+', '-' and '*']
    in random order."""
    operation_list = list(['sum', 'sub', 'mul'])
    shuffle(operation_list)
    return operation_list


def gen_operations_list(number_of_questions):
    """Generate list of math operations with the lenght
    more or equal number of questions in the game."""
    operations_list = make_operations_list_for_calc()
    len_list = len(operations_list)
    if number_of_questions > len_list:
        factor = (number_of_questions // len_list) + 1
    else:
        factor = 1
    new_list = list()
    new_list = factor * operations_list
    return new_list


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


def gen_game_data(number_of_questions: int):
    """Returns 2 lists with the equal lenghts
    len(list1) = len(list2) = number_of_questions.
    First list contains questions for the game.
    Second contains right answers on the same positions."""
    questions_list = list()
    right_answers_list = list()
    operations_list = gen_operations_list(number_of_questions)
    for questions_count in range(0, number_of_questions):
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        current_operation = operations_list[questions_count]
        operation_result = calc_operation_res(current_operation, num1, num2)
        question_content = make_task_txt(current_operation, num1, num2)
        question = 'Question: {}'.format(question_content)
        questions_list.append(question)
        right_answer = operation_result
        right_answers_list.append(right_answer)
    return questions_list, right_answers_list
