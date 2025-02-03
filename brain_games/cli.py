import random

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name


def greet():
    print("Welcome to the Brain Games!")


def it_is_an_even_number(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sum = 0
    for i in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        if num % 2 == 0:
            ans = prompt.string('Your answer: ')
            if ans == 'yes':
                print('Correct!')
                sum += 1
                continue
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        else:
            ans = prompt.string('Your answer: ')
            if ans == 'no':
                print('Correct!')
                sum += 1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
    if sum == 3:
        print(f'Congratulations, {name}!')