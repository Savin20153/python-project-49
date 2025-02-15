import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    count_divs = 0
    for div_1 in range(1, number + 1):
        if number % div_1 == 0:
            count_divs += 1
    if count_divs == 2:
        return True
    else:
        return False


def question_number_and_answer():
    question_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question_number = str(question_number)
    if is_prime(int(question_number)):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question_number, right_answer
