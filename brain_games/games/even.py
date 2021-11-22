from random import randint
import prompt
from brain_games.cli import print_message, bye_user


def isEven(number):
    return ((number % 2) == 0)


def even_main():

    k = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while k < 3:
        random_number = randint(1, 99)
        question = 'Question: ' + str(random_number)
        print(question)
        answer = prompt.string('Your answer: ')
        right_answer = 'yes' if isEven(random_number) else 'no'
        print_message(answer, right_answer)
        if answer == right_answer:
            k = k + 1
        else:
            k = 666
    if k == 3:
        bye_user()
