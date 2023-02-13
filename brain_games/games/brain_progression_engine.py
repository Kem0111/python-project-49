from random import randint


def br_progression():
    progression = (list(range(
        randint(1, 30),
        randint(70, 100),
        randint(2, 10)))[:10]
    )
    index = randint(1, len(progression) - 2)
    progression[index] = '..'
    string_progression = ' '.join([str(i) for i in progression])
    return string_progression


def true_answer(integer, answer):
    integer = integer.split(' ')
    num = 0
    for i in range(len(integer)):
        if integer[i] == '..':
            num += (int(integer[i-1])+int(integer[i+1]))//2
    if answer == str(num):
        return True
    else:
        return f"'{answer}' is wrong answer ;(. \
Correct answer was '{num}'."


def rules():
    return 'What number is missing in the progression?'
