from GuessGame import *
from MemoryGame import *
from CurrencyRouletteGame import *
from Scores import *


mem_game = "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
guess_game = "Guess Game - guess a number and see if you chose like the computer"
currency_game = "Currency Roulette - try and guess the value of a random amount of USD in ILS"

def welcome():
    name = input("pleas enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return name

def get_game():
    game_selection = f"Please choose a game to play:\n1. {mem_game}\n2. {guess_game}\n3. {currency_game}"
    while True:
        select_game = int(input(game_selection + "\nplease select a game: "))
        return select_game
        if select_game in range(0, 4):
            break

def get_difficulty():
    difficulty_selection = f"please select a difficulty level between 1-5: "
    while True:
        select_difficulty = int(input(difficulty_selection))
        if select_difficulty in range(0, 6):
            return select_difficulty
            break

def load_game():
    welcome()
    selected_game = get_game()
    selected_difficulty = get_difficulty()

    print(f"you have selected game number {selected_game} in difficulty level of {selected_difficulty}")
    game_result = None
    another_round = ""

    if selected_game == 1:
        game_result = play_memory(selected_difficulty, selected_game)
        if game_result == True:
            add_score(selected_difficulty, game_result, another_round)
            another_round = input("would you like to play another round? ")
            if another_round == "y":
                game_result = play_memory(selected_difficulty, selected_game)
                if game_result == True:
                    add_score(selected_difficulty, game_result, another_round)
        elif game_result == False:
            print("you lose")
            another_round = input("would you like to play another round? ")
            if another_round == "y":
                game_result
                add_score(selected_difficulty, game_result, another_round)
            elif another_round == "n":
                print("better luck next time")
            else:
                another_round

    elif selected_game == 2:
        game_result = play_guess(selected_difficulty, selected_game)
        if game_result == True:
            add_score(selected_difficulty, game_result, another_round)
            another_round = input("would you like to play another round? ")
            if another_round == "y":
                game_result = play_guess(selected_difficulty, selected_game)
                if game_result == True:
                    add_score(selected_difficulty, game_result, another_round)
        elif game_result == False:
            print("you lose")
            another_round = input("would you like to play another round? ")
            if another_round == "y":
                load_game()
                add_score(selected_difficulty, game_result, another_round)
            elif another_round == "n":
                print("better luck next time")
            else:
                another_round

    elif selected_game == 3:
        game_result = play_currency(selected_difficulty, selected_game)
        if game_result == True:
            add_score(selected_difficulty, game_result, another_round)
            another_round = input("would you like to play another round? ")
            if another_round == "y":
                game_result = play_currency(selected_difficulty, selected_game)
                if game_result == True:
                    add_score(selected_difficulty, game_result, another_round)
        elif game_result == False:
            print("you lose")
            another_round = input("would you like to play another round? ")
            if another_round == "y":
                load_game()
                add_score(selected_difficulty, game_result, another_round)
            elif another_round == "n":
                print("better luck next time")
            else:
                another_round




