import random

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_divisors(number):
    return [div for div in range(1, number + 1) if number % div == 0]


def ques_num_and_ans():
    num_one, num_two = random.randint(1, 100), random.randint(1, 100)
    num_one_dlvs = get_divisors(num_one)
    num_two_dlvs = get_divisors(num_two)
    
    common_divisors = set(num_one_dlvs).intersection(num_two_dlvs)
    right_ans = str(max(common_divisors))
    
    ques_num = f'{num_one} {num_two}' 
    return ques_num, right_ans
