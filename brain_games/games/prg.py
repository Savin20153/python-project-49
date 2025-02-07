import random


def ques_num_and_ans():
    len_prog = random.randint(5, 15)
    num_prog = random.randint(1, 100)
    prog_dif = random.randint(1, 50)
    prog_list = []
    for i in range(len_prog):
        num_prog = num_prog + prog_dif
        prog_list.append(num_prog)
    ind_e1 = random.randint(0, len_prog - 1)  
    right_ans = str(prog_list[ind_e1])
    prog_list[ind_e1] = '..'
    ques_num = ' '.join(map(str, prog_list))  
    return ques_num, right_ans