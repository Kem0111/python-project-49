from random import randint


def get_game_round_data():
    progression = (list(range(
        randint(1, 30),
        randint(70, 100),
        randint(2, 10)))[:10]
    )
    index = randint(1, len(progression) - 2)
    number = progression[index]
    progression[index] = '..'
    string_progression = ' '.join([str(i) for i in progression])
    return string_progression, number


def RULSE():
    return 'What number is missing in the progression?'
