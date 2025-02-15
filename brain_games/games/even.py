import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def question_and_answer():
    question_number = random.randint(MIN_NUMBER, MAX_NUMBER)  
    if is_even(question_number): 
        right_answer = 'yes'  
    else:
        right_answer = 'no'   
    return question_number, right_answer