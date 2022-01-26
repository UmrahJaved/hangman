


class Hangman:

    def __init__(self, word_to_find):
        self.word_to_find = word_to_find

    def play(self, word_to_find):

        turn_count = 0
        error_count = 0
        lives = 5
        guess_letters = []
        for letter in word_to_find:
            guess_letters.append("_")
        print(guess_letters)
        well_guessed_letters = guess_letters
        wrongly_guessed_letters = []
        while (lives) > 0:
            if word_to_find == well_guessed_letters:
                print("Well Done!")
                break

            print(f"You have : {lives} lives")
            user_input = input("Guess the letter:").upper()
            turn_count = turn_count + 1
            print(f"Turn count: {turn_count}")

        # letter found - replce_by letter
            if user_input in word_to_find:

                for count in range(len(word_to_find)):
                    if user_input == word_to_find[count]:
                        well_guessed_letters[count] = user_input
                print(well_guessed_letters)
            else:
                error_count = error_count + 1
                lives = lives - 1
                print("Sorry, but it is wrong!")
                wrongly_guessed_letters.append(user_input)
                print(f"Wrong letters: {wrongly_guessed_letters}")

        return well_guessed_letters, wrongly_guessed_letters, lives, error_count, turn_count

    def game_over(self, lives):
        if (lives) == 0:
            print("Game Over!")

    def well_played(self, well_guessed_letters, turn_count, error_count):
        if well_guessed_letters == self.word_to_find:
            print(f"You found the word: {well_guessed_letters} in {turn_count} turns with {error_count} errors!.")


