# importing modules
import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

#printing logo
print(logo)

# setting lives
game_is_finished = False
lives = len(stages) - 1

#choosing a random word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# displaying empty string according to the  random word
display = []
for _ in range(word_length):
    display += "_"

# starting the game
while not game_is_finished:
    # receiving user guess
    guess = input("Guess a letter: ").lower()

    # clearing the previous outputs
    clear()

    # checking the character is already guessed or not
    if guess in display:
        print(f"You've already guessed {guess}")

    # comparing character with random word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    # if guessed character is not in the word reducing live by 1
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # if user runs out of lives the game stops
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    #if user completed the word the game stops
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])