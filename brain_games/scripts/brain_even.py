#!/usr/bin/env python3
from brain_games.games.implementation_br_even import\
    br_even, rules_br_even
from brain_games.engine_of_games import general_engine


def main():
    general_engine(br_even, rules_br_even)


if __name__ == '__main__':
    main()
