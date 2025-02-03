import random

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name


def greet():
    print("Welcome to the Brain Games!")


def false_ans(false_ans, current_ans, name):
    print(f"'{false_ans}' is wrong answer ;(. Correct answer was '{current_ans}'.")
    print(f"Let's try again, {name}!")


def enter_ans():
    ans = prompt.string('Your answer: ')
    return ans


def congratulations(name):
    print(f'Congratulations, {name}!')


def correct(sum):
    print('Correct!')
    sum += 1
    return sum


def it_is_an_even_number(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sum = 0
    for i in range(3):
        num = random.randint(1, 100)
        print(f'Question: {num}')
        if num % 2 == 0:
            ans = enter_ans()
            if ans == 'yes':
                correct(sum)
                continue
            else:
                false_ans(ans, 'yes', name)
                break
        else:
            ans = enter_ans()
            if ans == 'no':
                correct(sum)
            else:
                false_ans(ans, 'no', name)
                break
    if sum == 3:
        congratulations(name)


def is_this_calculated_correctly(name):
    print('What is the result of the expression?')
    sum = 0 
    all_signs = ['+', '-', '*']
    for i in range(3):
        num_one = random.randint(1, 100)
        num_two = random.randint(1, 100)
        sign_ind = random.randint(0, 2)
        sign = all_signs[sign_ind]
        expres_str = f'{num_one} {sign} {num_two}'
        print(f'Question: {expres_str}')
        expres_ans = eval(expres_str)
        ans = enter_ans()
        if int(ans) == expres_ans:
            correct(sum)
            continue
        else:
            false_ans(ans, expres_ans, name)
            break
    if sum == 3:
        congratulations(name)