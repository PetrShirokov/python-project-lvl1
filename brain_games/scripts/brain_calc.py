#!/usr/bin/env python


from brain_games.games.calc import TASK_MESSAGE as task
from brain_games.games.calc import gen_game_data
from brain_games.game_logic import play_game


def main():
    NUMBER_OF_QUESTIONS = 3
    questions_list, right_answers_list = gen_game_data(NUMBER_OF_QUESTIONS)
    play_game(task, questions_list, right_answers_list)


if __name__ == "__main__":
    main()
