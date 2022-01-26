import random

class Hangman:

    possible_words= ["Becode","Learning","Mathematics","Sessions","Computer","Machine","Bruxelles","Belgium"]

    word_to_find= list(random.choice(possible_words).upper())


    lives=5

    guess_letters= []
    for i in word_to_find:
        guess_letters.append("_")
    print(guess_letters)
    correctly_guessed_letters=guess_letters

    turn_count=0
    error_count=0
    while (lives-error_count)>0:

        # exact match- break
        if word_to_find==correctly_guessed_letters:
               print("Well Done!")
               break
        print(f"Lives:{lives-error_count} lives")
        user_input = input("Guess the letter:").upper()
        turn_count=turn_count+1
        print(f"Turn count: {turn_count}")

        # letter found - replce_by letter
        if user_input in word_to_find:
            for count in range(len(word_to_find)):
                if user_input== word_to_find[count]:
                    correctly_guessed_letters[count]=user_input
            print(correctly_guessed_letters)
        # letter not found- lives=lives-1
        else:
            error_count=error_count+1
            print("Sorry, but it is wrong!")
            #print(f"You are left with {lives-error_count} lives")
            error_count
            wrongly_guessed_letters=[]
            wrongly_guessed_letters.append(user_input)
            print(f"Wrong letters: {wrongly_guessed_letters}")


    if (lives-error_count)==0:
        print("Better luck next time")










