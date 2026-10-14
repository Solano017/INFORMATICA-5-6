def main():
    print("-----------Kahoot-----------")
    print("Welcome to: Times Table Quiz")
    while True:
        try:
            times_table = int(input("Enter a times table you would like to get tested from 1 to 10: "))
            break
        except ValueError:
            print("please enter a number")
    while True:
        try:
            max_value = int(input("Enter the maximum value for your times table: "))
            max_value += 1
            break
        except ValueError:
            print("Please enter a number")
    score = 0
    if 1 <= times_table <= 10:
        print(f"Here is your quiz on the {times_table} times table")
        while True:
            for x in range(1, max_value):
                try:
                    answer = x * times_table
                    print(f"{times_table} times {x} is equal to?")
                    user_answer = int(input("Answer: "))
                    if user_answer == answer:
                        print(f"{x} times {times_table} is {answer}")
                        print("Correct")
                        score += 1
                        print(f"your score is, {score}")
                    else:
                        print(f"{x} times {times_table} is {answer}")
                        print("Incorrect")
                        print(f"actual score is: {score}")
                except ValueError:
                    print("Invalid")
            break

    else:
        print("Times Table has to be between 1 to 10, not higher nor lower.")
        print("Try again pls")


if __name__ == "__main__":
    main()

    # letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # aletters = []
    # lives = 6
    # while lives != 0:
    #     print("Hi")

    # # start_game()

    # # def start_game(file):

import random

# List of words to choose from
words = ["python", "developer", "hangman", "programming", "computer", "algorithm"]

def play_hangman():
    # Pick a random word
    word = random.choice(words)
    word_letters = set(word)  # letters in the word
    guessed_letters = set()   # what the user has guessed
    lives = 6                 # number of allowed wrong tries

    print("Welcome to Hangman!")

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Display current guessed letters
        print(f"\nYou have {lives} lives left.")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Display word with underscores for hidden letters
        word_list = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))

        # Get user input
        user_guess = input("Guess a letter: ").lower()

        # Validate input
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if user_guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(user_guess)

        if user_guess in word_letters:
            word_letters.remove(user_guess)
            print(f"Good job! '{user_guess}' is in the word.")
        else:
            lives -= 1
            print(f"Sorry, '{user_guess}' is not in the word.")

    # End of game results
    if lives == 0:
        print(f"\nGame over! The word was '{word}'.")
    else:
        print(f"\nCongratulations! You guessed the word '{word}' correctly!")

if __name__ == "__main__":
    play_hangman()

import random
def main():
    # Create a TXT file with all of the words.
    # Define the main function
    # Give a welcome message
    # Use with to open the TXT file
    # Input to ask user for the letter
    # Have a list to know what letters have been already used
    # Not allow the user to input more than one word unless he is trying to already guess the word using len
    # print the list of already used apps
    # use a function to make the words.txt into a list
    # use an updating value for the lifes
    # use a while loop to repeat our code
    # use a for loop to condition changes
    # use the random function to select a random word from our list
    # reveal the word after losing or winning
    # import random so we can randomize the word
    #
    with open("words.txt") as words:
        random = words.read().splitlines()
        randw = random.r(random)
        print(randw)



    print (word)
    # use an if statement to check if the player wins
    # ask the player if they want to play again
if __name__ == "__main__":
    main()
