#!/usr/bin/env python


from brain_games.games.calc import TASK_MESSAGE as task
from brain_games.games.calc import gen_game_data as game_data
from brain_games.game_logic import play_game


def main():
    play_game(task, game_data)


if __name__ == "__main__":
    main()
