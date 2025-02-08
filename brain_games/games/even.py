import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def ques_num_and_ans():
    ques_num = random.randint(1, 100)  
    if ques_num % 2 == 0:  
        right_ans = 'yes'  
    else:
        right_ans = 'no'   
    return ques_num, right_ans  