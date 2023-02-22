#!/usr/bin/env python3
from brain_games.engine_of_games import general_engine
from brain_games.games.implementation_brain_progression import br_progression,\
    rules_br_progression


def main():
    general_engine(br_progression, rules_br_progression)


if __name__ == '__main__':
    main()
