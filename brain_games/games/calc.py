import random


def ques_num_and_ans():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    sign = random.choice(['+', '-', '*'])
    ques_num = f'{num_one} {sign} {num_two}'
    right_ans = str(eval(ques_num))  
    return ques_num, right_ans