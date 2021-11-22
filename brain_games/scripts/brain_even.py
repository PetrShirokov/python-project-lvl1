#!/usr/bin/env python
from brain_games import cli
from brain_games.games import even


def main():
    cli.print_before_welcome()
    cli.welcome_user()
    even.even_main()


if __name__ == '__main__':
    main()
