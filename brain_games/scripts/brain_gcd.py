#!/usr/bin/env python
from brain_games.cli import print_before_welcome, welcome_user
from brain_games.games.gcd import game_gcd


def main():
    print_before_welcome()
    welcome_user()
    game_gcd()


if __name__ == '__main__':
    main()
