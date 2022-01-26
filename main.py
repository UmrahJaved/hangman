from utils.game import Hangman
import random


possible_words = ["Becode", "Learning", "Mathematics", "Sessions", "Computer", "Machine", "Bruxelles", "Belgium"]
word_to_find = list(random.choice(possible_words).upper())

objHangman=Hangman(word_to_find)

#funcPlayReturn=objHangman.play(word_to_find)
#objHangman.game_over(funcPlayReturn[2])
#objHangman.well_played(funcPlayReturn[0],funcPlayReturn[4],funcPlayReturn[3])

def start_game():
    funcPlayReturn = objHangman.play(word_to_find)
    objHangman.game_over(funcPlayReturn[2])
    objHangman.well_played(funcPlayReturn[0], funcPlayReturn[4], funcPlayReturn[3])

start_game()