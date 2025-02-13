import random

QUESTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 100


def calculation(number_1, number_2, operation):
    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    else:
        return number_1 * number_2


def question_number_and_answer():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(['+', '-', '*'])
    question_number = f'{number_1} {operation} {number_2}' 
    right_answer = str(calculation(number_1, number_2, operation))
    return question_number, right_answer