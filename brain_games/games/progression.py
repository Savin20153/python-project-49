import random

QUESTION = 'What number is missing in the progression?'

MIN_LEN_PROGRESSION = 5
MAX_LEN_PROGRESSION = 15
MIN_NUMBER = 1
MAX_NUMBER = 100


def question_and_answer():
    len_progression = random.randint(MIN_LEN_PROGRESSION, MAX_LEN_PROGRESSION)
    number_progression = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression_difference = random.randint(MIN_NUMBER, MAX_NUMBER)
    progression_list = []
    for _ in range(len_progression):
        number_progression = number_progression + progression_difference
        progression_list.append(number_progression)
    index_missing_number = random.randint(0, len_progression - 1)
    right_answer = str(progression_list[index_missing_number])
    progression_list[index_missing_number] = '..'
    question_number = ' '.join(map(str, progression_list))
    return question_number, right_answer