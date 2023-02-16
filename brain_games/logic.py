import prompt


def questions(func, rules, true_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules())
    a = 0
    for _ in range(3):
        number = func()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        is_answer_true = true_answer(number)
        if answer == str(is_answer_true):
            print('Correct')
            a += 1
        else:
            print(
                f"""'{answer}' is wrong answer ;(.
                Correct answerwas '{str(is_answer_true)}'."""
                )
            print(f"Let's try again, {name}!")
            break
    if a == 3:
        print(f'Congratulations, {name}!')
