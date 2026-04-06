import random

# List of words
words = ["python", "hangman", "computer", "program"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        attempts -= 1
        guessed_letters.append(guess)

    # Check if all letters are guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

# If attempts finished
if attempts == 0:
    print("\nGame Over! The word was:", word)
