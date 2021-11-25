#!/usr/bin/env python

from brain_games.cli import print_before_welcome
from brain_games.cli import welcome_user
from brain_games.games.progression import game_progression


def main():
    print_before_welcome()
    welcome_user()
    game_progression()


if __name__ == "__main__":
    main()
