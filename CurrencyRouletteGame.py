from currency_converter import CurrencyConverter
from random import *
import numpy as np

def get_money_interval(selected_difficulty):
    converted = CurrencyConverter().convert(1, 'USD', 'ILS')
    d = selected_difficulty
    dollars = randint(1, 100)
    t = dollars * converted
    print(t)
    interval = np.arange((t - (5 - d)), (t + (5 - d)), 0.1)
    return [dollars, t, interval]

def get_user_guess(dollars):
    user_guess = float(input(f"can you guess what is the value of {dollars}$ in Shekels? "))
    return user_guess

def compare_lists(t, interval, user_guess):
    if user_guess > interval[0] and user_guess < interval[-1]:
        return True
    else:
        return False

def play_currency(selected_difficulty, selected_game):
    dollars, t, interval = get_money_interval(selected_difficulty)
    user_guess = get_user_guess(dollars)
    if compare_lists(t, interval, user_guess) == True:
        return True
    else:
        return False
