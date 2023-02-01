from random import randint
import prompt


def br_progression():
    print('What number is missing in the progression?')
    progression = list(range(randint(1, 30), randint(70, 100),
                             randint(2, 10)))[:10]
    index = randint(0, len(progression) - 1)
    random_int = progression[index]
    progression[index] = '..'
    string_progression = ' '.join([str(i) for i in progression])
    print(f'Question: {string_progression}')
    answer = prompt.string('Your answer: ')
    if answer == str(random_int):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{random_int}'.")
        return False
