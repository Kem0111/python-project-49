#!/usr/bin/env python3
from brain_games.games import implementation_brain_prime
from brain_games.engine_of_games import general_engine


def main():
    general_engine(
        implementation_brain_prime.br_prime,
        implementation_brain_prime.rules_br_prime
        )


if __name__ == '__main__':
    main()
