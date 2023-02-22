#!/usr/bin/env python3
from brain_games.engine_of_games import general_engine
from brain_games.games.implementation_br_calc import\
    br_calc, rules_br_calc


def main():
    general_engine(br_calc, rules_br_calc)


if __name__ == '__main__':
    main()
