import random as rd
import string
from sys import argv, exit


def gen_seeds(pw_len):
    seed_list_fun = []
    while len(seed_list_fun) < pw_len:
        seed_list_fun.append(int(rd.randint(1, 4)))

    return seed_list_fun


if __name__ == '__main__':
    L_CASE = string.ascii_lowercase
    U_CASE = string.ascii_uppercase
    SPECIAL = ['!', '?', '=', '+', '-', '*', '$', '|', ':', '%']
    NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    CASES_DICT = {'1': L_CASE, '2': U_CASE, '3': SPECIAL, '4': NUM}
    CASES_LIST = [1, 2, 3, 4]

    pw_length = int(argv[1])

    if pw_length < 4:
        print('Please define a password length of minimum 4 characters\n')
        exit()
    elif pw_length > 24:
        print('Please define a password length of maximal 24 characters\n')
        exit()

    seed_list = gen_seeds(pw_length)

    while not all(item in seed_list for item in CASES_LIST):
        seed_list = gen_seeds(pw_length)

    pw_output = ''
    for seed in seed_list:
        pw_output += CASES_DICT[str(seed)][rd.randint(0, len(CASES_DICT[str(seed)])-1)]

    print(f'Generated Password with {pw_length} characters: {pw_output}\n')