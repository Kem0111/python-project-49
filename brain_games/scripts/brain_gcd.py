#!/usr/bin/env python3
from brain_games.engine_of_games import general_engine
from brain_games.games.implementation_br_gcd import br_gcd,\
    rules_br_gcd


def main():
    general_engine(br_gcd, rules_br_gcd)


if __name__ == '__main__':
    main()
