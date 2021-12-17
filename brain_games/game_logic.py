import prompt


def play_game(task, gen_game_data):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    hi_string = 'Hello, {}!'.format(name)
    print(hi_string)
    print(task)
    questions_count = 0
    NUMBER_OF_QUESTIONS = 3
    while (questions_count < NUMBER_OF_QUESTIONS):
        current_question, right_answer = list(gen_game_data())
        full_question = 'Question: {}'.format(current_question)
        print(full_question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            sentence1 = ("'{}' is a wrong answer ;(. ").format(user_answer)
            sentence2 = ("Correct answer was '{}'. ").format(right_answer)
            sentence3 = ("Let's try again, {}!").format(name)
            message = sentence1 + sentence2 + sentence3
            print(message)
            return
        questions_count += 1
    congratulation_string = "Congratulations, {}!".format(name)
    print(congratulation_string)
