import prompt
from random import randint, shuffle
from brain_games.cli import bye_user
from brain_games.cli import print_message, print_question
from brain_games.logic import calc_operation_res


def game_calc():
    operation_lst = list(['sum', 'sub', 'mul'])
    shuffle(operation_lst)
    k = 0
    while k < 3:
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        current_operation = operation_lst.pop()
        print_question(current_operation, num1, num2)
        user_answer = prompt.string('Your answer: ')
        operation_result = calc_operation_res(current_operation, num1, num2)
        right_answer = str(operation_result)
        print_message(user_answer, right_answer)
        if user_answer == right_answer:
            k = k + 1
        else:
            k = 666
    if k == 3:
        bye_user()
