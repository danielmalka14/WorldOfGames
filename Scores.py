from Utils import *
from Live import *

def add_score(selected_difficulty, game_result, another_round):
    POINTS_OF_WINNING = (selected_difficulty * 3) * 5

    try:
        if game_result == True:
            with SCORES_FILE_NAME as write_scores:
                write = write_scores.write(str(POINTS_OF_WINNING))

        if another_round == "y" and game_result == True:
            with open("Scores.txt", 'w+') as write_again:
                int_score = int(write_again.readline())
                print(int_score)
                int_score += POINTS_OF_WINNING
                print(int_score)
                print(type(int_score))
                write_score = write_again.write(str(int_score))

    except Exception as BAD_RETURN_CODE:
        print(BAD_RETURN_CODE)
        if game_result == True:
            with open("alt_score.txt", 'w+') as new_score:
                write_score = new_score.write(str(POINTS_OF_WINNING))

        if another_round == "y" and game_result == True:
            with open("alt_score.txt", 'r+') as read_score:
                int_score = int(read_score.readline())
                int_score += POINTS_OF_WINNING
                read_score.close()
                additional_score = open(r"alt_score.txt", "w")
                total = additional_score.write(str(int_score))













