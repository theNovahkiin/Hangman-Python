import random

hangman = ["___", " |", " |", " O", "/|\ ", " |", "/ \ "] #hangman parts
word_lib = [
    "python", "blanket", "start", "righteous", "brain", "invoke", "submit", "stir", "ring", "recurrent", "bargain", "morning", "night"
] #list of words for the game
word_select = random.randint(0, len(word_lib) - 1) #selection of words from random index of the list
word = word_lib[word_select] #word to guess
blanks = "_"
letter_list = list(word) #list of letters in the word
guess_list = [] #list for adding correct letters by user
incorrect_list = [] #list for adding incorrect letters by user
hangman_parts = [] #list for adding hangman parts when guess is incorrect
wrong_guesses = 0 #number of wrong answers

print("WELCOME TO HANGMAN.")
print("The word is of {} letters.".format(len(word)))

#generating blanks corresponding the number of letters in the word
for num_of_letters in range(0, len(word)):
    guess_list.append(blanks)
print(' '.join(guess_list))

#game loop
while wrong_guesses <= len(hangman) - 1:
    #condition for when the word to guess does not exist
    if len(word) == 0:
        break
    user = input("Guess a letter or the whole word: ")
    #condition for when player guesses the whole word correctly
    if user == word:
        print("You win!!")
        break
    #condition for when player enters previously guessed incorrect letter
    while user in incorrect_list:
        print("Already guessed. Guess another letter.")
        user = input("Guess a letter or the whole word: ")
    #condition for checking if the letter player guesses is in the word
    if user in word:
        #loop for getting index of every letter in the word
        for index, letter in enumerate(word):
            #condition for filling the correct letters the player guesses into guess_list
            if letter == user:
                guess_list[index] = letter
        #condition for when player correctly guesses all the letters of the word
        if guess_list == letter_list:
            print("You win.")
            print(" ".join(guess_list))
            break
        print("Correct.")
        print(" ".join(guess_list))
    #condition for when the guess is incorrect
    else:
        print("Incorrect.")
        incorrect_list.append(user)
        #loop for adding hangman components to a list as incorrect guesses are entered
        hangman_parts.append(hangman[wrong_guesses])
        for i in range(0, len(hangman_parts)):
            print(hangman_parts[i])

        wrong_guesses += 1
        #condition for when the hangman is complete
        if wrong_guesses == len(hangman):
            print("You lose.")
            print("The word was {}.".format(word.upper()))
            break
