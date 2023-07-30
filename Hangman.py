hangman = ["___", " |", " |", " O", "/|\ ", " |", "/ \ "]
word = "nice"
blanks = "_"
letter_list = list(word) #list of letters in the word
guess_list = [] #list for adding correct letter guesses by user
hangman_parts = [] #list for adding hangman parts when guess is incorrect
wrong_guesses = 0 #number of wrong answers
score = 0 #player score

print("The word is of {} letters.".format(len(word)))

#generating blanks corresponding the number of letters in the word
for num_of_letters in range(0, len(word)):
    guess_list.append(blanks)
print(' '.join(guess_list))

#game loop
while wrong_guesses <= len(hangman) - 1:
    if len(word) == 0:
        break
    user = input("Guess a letter or the whole word: ")
    if user == word:
        print('You won!!')
        break

    if user in word:
        for index, letter in enumerate(word):
            if letter == user:
                guess_list[index] = letter
        if guess_list == letter_list:
            print("You won.")
            print(" ".join(guess_list))
            break
        print(" ".join(guess_list))

    else:
        print("Incorrect. Try Again.")
        #adding hangman components to a list as incorrect guesses are entered and printing the newly created list items
        hangman_parts.append(hangman[wrong_guesses])
        for i in range(0, len(hangman_parts)):
            print(hangman_parts[i])

        wrong_guesses += 1
        if wrong_guesses == len(hangman):
            print('You lose.')
            break

