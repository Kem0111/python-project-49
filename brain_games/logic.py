import prompt


def questions(func, rules, true_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules())
    a = 0
    for i in range(3):
        number = func()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        is_answer_true = true_answer(number, answer)
        if is_answer_true is True:
            print('Correct')
            a += 1
        else:
            print(is_answer_true)
            print(f"Let's try again, {name}!")
            break
    if a == 3:
        print(f'Congratulations, {name}!')
