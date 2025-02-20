import math
import random

QUESTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question_and_answer():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = str(math.gcd(number_1, number_2))
    question = f'{number_1} {number_2}' 
    return question, right_answer