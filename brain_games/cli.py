import prompt


def welcome_user():
    global name
    name = prompt.string("May I have your name? ")
    hi_string = 'Hello, {}!'.format(name)
    print(hi_string)


def congratulate_user():
    congratulation_string = "Congratulations, {}!".format(name)
    print(congratulation_string)


def print_response_message(user_answer, right_answer):
    if user_answer == right_answer:
        message = 'Correct!'
    else:
        sentence1 = ("'{}' is a wrong answer ;(. ").format(user_answer)
        sentence2 = ("Correct answer was '{}'. ").format(right_answer)
        sentence3 = ("Let's try again, {}!").format(name)
        message = sentence1 + sentence2 + sentence3
    print(message)
