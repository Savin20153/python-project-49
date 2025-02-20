import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False
    for division in range(2, int(number ** 0.5) + 1):
        if number % division == 0:
            return False
    return True


def generate_question_and_answer():
    question_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question_number = str(question_number)
    if is_prime(int(question_number)):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question_number, right_answer
