#!/usr/bin/env python

from brain_games.cli import print_before_welcome, print_first_game_message
from brain_games.cli import welcome_user
from brain_games.games.calc import game_calc


def main():
    print_before_welcome()
    welcome_user()
    print_first_game_message()
    game_calc()


if __name__ == "__main__":
    main()
