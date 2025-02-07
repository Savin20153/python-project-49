import random


def ques_num_and_ans():
    ques_num = random.randint(1, 100)
    divs = []
    for div_one in range(1, ques_num + 1):
        if ques_num % div_one == 0:
            divs.append(ques_num)
    ques_num = str(ques_num)
    if len(divs) == 2:
        right_ans = 'yes'
        return ques_num, right_ans
    else:
        right_ans = 'no'
        return ques_num, right_ans