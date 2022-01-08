from random import *

def generate_number(selected_difficulty):
    secret_number = randint(0, selected_difficulty)
    print(secret_number)
    return secret_number

def get_guess_from_user(selected_difficulty):
    user_guess = int(input(f"please guess a number between 1 to {selected_difficulty} :"))
    if user_guess in range(0, selected_difficulty):
        return user_guess

def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False

def play_guess(selected_difficulty, selected_game):
    secret_number = generate_number(selected_difficulty)
    user_guess = get_guess_from_user(selected_difficulty)
    if compare_results(secret_number, user_guess) == True:
        return True
    else:
        return False



