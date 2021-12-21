import prompt


def play_game(task, gen_game_data):
    print('Welcome to the Brain Games!')
    name = prompt.string("May I have your name? ")
    print('Hello, {}!'.format(name))
    print(task)
    for question_number in range(3):
        current_question, right_answer = gen_game_data()
        print('Question: {}'.format(current_question))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            print("'{}' is a wrong answer ;(. "
                  "Correct answer was '{}'.\n"
                  "Let's try again, {}!".format(answer, right_answer, name))
            return
    print("Congratulations, {}!".format(name))
