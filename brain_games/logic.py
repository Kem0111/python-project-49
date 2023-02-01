import prompt


def questions(funk):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    a = 0
    for i in range(3):
        if funk() is False:
            a += 1
            print(f"Let's try again, {name}!")
            break
    if a == 0:
        print(f'Congratulations, {name}!')
