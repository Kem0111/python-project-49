#!/usr/bin/env python3
from brain_games.games.implementation_brain_prime import br_prime,\
    rules_br_prime
from brain_games.engine_of_games import general_engine


def main():
    general_engine(br_prime, rules_br_prime)


if __name__ == '__main__':
    main()
