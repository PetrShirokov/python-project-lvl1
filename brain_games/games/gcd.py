from random import randint
import prompt
from brain_games.cli import print_message, bye_user
from brain_games.logic import max_common_divisor


def game_gcd():
    k = 0
    print('Find the greatest common divisor of given numbers.')
    while k < 3:
        number1 = randint(1, 99)
        number2 = randint(1, 99)
        question = 'Question: {} {}'.format(number1, number2)
        print(question)
        answer = prompt.string('Your answer: ')
        right_answer = str(max_common_divisor(number1, number2))
        print_message(answer, right_answer)
        if answer == right_answer:
            k = k + 1
        else:
            k = 666
    if k == 3:
        bye_user()
