#!/usr/bin/env python3
from brain_games.engine_of_games import general_engine
from brain_games.games import implementation_brain_progression


def main():
    general_engine(
        implementation_brain_progression.br_progression,
        implementation_brain_progression.rules_br_progression
        )


if __name__ == '__main__':
    main()
