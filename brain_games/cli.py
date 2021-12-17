import prompt


def welcome_user():
    global name
    name = prompt.string("May I have your name? ")
    hi_string = 'Hello, {}!'.format(name)
    print(hi_string)
