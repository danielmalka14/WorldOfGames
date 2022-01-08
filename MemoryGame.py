from random import *
from Utils import screen_cleaner
import time

def generate_sequence(selected_difficulty):
    rand_sequence = [randrange(0, 103) for x in range(selected_difficulty)]
    print(rand_sequence)
    time.sleep(0.7)
    screen_cleaner
    return rand_sequence

def get_list_from_user():
    user_guess = input("please guess the numbers list you just reviewed:").split()
    user_list = [int(x) for x in user_guess]
    return user_list

def is_list_equal(rand_sequence, user_list):
    if rand_sequence == user_list:
        return True
    else:
        return False

def play_memory(selected_difficulty, selected_game):
    rand_sequence = generate_sequence(selected_difficulty)
    user_list = get_list_from_user()
    if is_list_equal(rand_sequence, user_list) == True:
        return True
    else:
        return False