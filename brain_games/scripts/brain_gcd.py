#!/usr/bin/env python3
from brain_games.engine_of_games import general_engine
from brain_games.games import implementation_br_gcd


def main():
    general_engine(
        implementation_br_gcd.br_gcd,
        implementation_br_gcd.rules_br_gcd
    )


if __name__ == '__main__':
    main()
