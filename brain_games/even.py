from random import randint
import prompt

number = 0
name = ''


def welcome_user():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    hi_string = 'Hello, {}!'.format(name)
    print(hi_string)
    return name


def isEven(number):
    return ((number % 2) == 0)


def isCorrect(answer):
    return (isEven(number) == answer)


def even_main():

    k = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while k < 3:
        random_number = randint(1, 99)
        prompt_str = 'Question: ' + str(random_number)
        print(prompt_str)
        answer = prompt.string('Your answer: ')
        right_answer = 'yes' if isEven(random_number) else 'no'
        if (answer == right_answer):
            k = k + 1
            print('Correct!')
        else:
            k = 4
            out_message1 = ("'{}' is a wrong answer ;(. ").format(answer)
            out_message2 = ("Correct answer was '{}'. ").format(right_answer)
            out_message3 = ("Let's try again, {}!").format(name)
            print(out_message1 + out_message2 + out_message3)
    if k == 3:
        print('Congratulations, ' + name + '!')
