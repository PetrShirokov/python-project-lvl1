import prompt


def print_before_welcome():
    zero_message = 'Welcome to the Brain Games!'
    print(zero_message)


def welcome_user():
    global name
    name = prompt.string("May I have your name? ")
    hi_string = 'Hello, {}!'.format(name)
    print(hi_string)


def bye_user():
    bye_string = "Congratulations, {}!".format(name)
    print(bye_string)


def print_first_game_message():
    first_game_message = 'What is the result of the expression?'
    print(first_game_message)


def print_message(answer, right_answer):
    if answer == right_answer:
        message = 'Correct!'
    else:
        sentence1 = ("'{}' is a wrong answer ;(. ").format(answer)
        sentence2 = ("Correct answer was '{}'. ").format(right_answer)
        sentence3 = ("Let's try again, {}!").format(name)
        message = sentence1 + sentence2 + sentence3
    print(message)


def print_question(operation, num1, num2):
    if operation == 'sum':
        text = ('{} + {}').format(num1, num2)
    elif operation == 'sub':
        max_num = max(num1, num2)
        min_num = min(num1, num2)
        text = ('{} - {}').format(max_num, min_num)
    elif operation == 'mul':
        text = ('{} * {}').format(num1, num2)
    question = 'Question: ' + text
    print(question)
