from random import randint
import prompt
from brain_games.cli import welcome_user, congratulate_user
from brain_games.cli import print_response_message
from brain_games.games.progression import gen_progression_with_hidden_member
from brain_games.games.even import is_even
from brain_games.games.prime import is_prime
from brain_games.games.gcd import max_common_divisor
from brain_games.games.calc import choose_operation_for_calc, calc_operation_res
from brain_games.games.calc import make_task_txt


def print_head_message():
    head_message = 'Welcome to the Brain Games!'
    print(head_message)


def print_task_message(game_name):
    if game_name == 'even':
        text = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game_name == 'prime':
        text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    elif game_name == 'gcd':
        text = 'Find the greatest common divisor of given numbers.'
    elif game_name == 'calc':
        text = 'What is the result of the expression?'
    elif game_name == 'progression':
        text = 'What number is missing in the progression?'
    print(text)


def generate_question(game_name):
    global right_answer
    if game_name == 'progression':
        progression_list = gen_progression_with_hidden_member()
        task_for_question = str(progression_list[0])
        right_answer = str(progression_list[1])
    elif game_name == 'even':
        random_number = randint(1, 99)
        task_for_question = str(random_number)
        right_answer = str(is_even(random_number))
    elif game_name == 'prime':
        random_number_for_prime = randint(2, 50)
        task_for_question = str(random_number_for_prime)
        right_answer = str(is_prime(random_number_for_prime))
    elif game_name == 'gcd':
        number1 = randint(1, 99)
        number2 = randint(1, 99)
        task_for_question = '{} {}'.format(number1, number2)
        right_answer = str(max_common_divisor(number1, number2))
    elif game_name == 'calc':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        current_operation = choose_operation_for_calc()
        operation_result = calc_operation_res(current_operation, num1, num2)
        task_for_question = make_task_txt(current_operation, num1, num2)
        right_answer = str(operation_result)
    full_task = 'Question: {}'.format(task_for_question)
    print(full_task)


def receive_the_answer():
    global user_answer
    user_answer = prompt.string('Your answer: ')


def play_game(game_name):
    print_head_message()
    welcome_user()
    print_task_message(game_name)
    questions_count = 0
    MAX_NUMBER_OF_QUESTIONS = 3
    while (questions_count < MAX_NUMBER_OF_QUESTIONS):
        questions_count += 1
        generate_question(game_name)
        receive_the_answer()
        print_response_message(user_answer, right_answer)
        if (user_answer != right_answer):
            break
        if questions_count == MAX_NUMBER_OF_QUESTIONS:
            congratulate_user()
