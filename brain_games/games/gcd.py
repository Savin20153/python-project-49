import random

QUESTION = 'Find the greatest common divisor of given numbers.'


def ques_num_and_ans():
    num_one, num_two = random.randint(1, 100), random.randint(1, 100)
    num_one_divs, num_two_divs = [], []
    
    for div_one in range(1, num_one + 1):
        if num_one % div_one == 0:
            num_one_divs.append(div_one)
    
    for div_two in range(1, num_two + 1):
        if num_two % div_two == 0:
            num_two_divs.append(div_two)
    
    intersection_list = set(num_one_divs).intersection(num_two_divs)
    right_ans = str(max(intersection_list))
    ques_num = f'{num_one} {num_two}' 
    return ques_num, right_ans
