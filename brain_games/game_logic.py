import prompt
from brain_games.cli import welcome_user, congratulate_user
from brain_games.cli import print_response_message


def print_head_message():
    head_message = 'Welcome to the Brain Games!'
    print(head_message)


def print_task_message(task):
    print(task)


def receive_the_answer():
    global user_answer
    user_answer = prompt.string('Your answer: ')


def play_game(task, questions_list, right_answers_list):
    print_head_message()
    welcome_user()
    print_task_message(task)
    questions_count = 0
    upper_index_of_questions_list = len(questions_list) - 1
    while (questions_count <= upper_index_of_questions_list):
        current_question = questions_list[questions_count]
        print(current_question)
        receive_the_answer()
        right_answer = str(right_answers_list[questions_count])
        print_response_message(user_answer, right_answer)
        if (user_answer != right_answer):
            break
        if questions_count == upper_index_of_questions_list:
            congratulate_user()
        questions_count += 1
