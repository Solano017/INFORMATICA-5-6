import random

def main():
    Name = input("Hey! What is your name? ")



    print("Difficulty Levels:")
    print("Easy 1-10")
    print("Medium 1-1000")
    print("Hard 1-1000000")

    level = input("Choose a difficulty level: ").strip().lower()
    if level == ("easy"):
        print("You selected level", level)
        guess = random.randint(1, 10)
        print("Well,", Name, "I am thinking of a number in between 1 and 10.")

    if level == ("medium"):
        print("You selected level", level)
        guess = random.randint(1, 1000)
        print("Well,", Name, "I am thinking of a number in between 1 and 1000.")

    if level == ("hard"):
        print("You selected level", level)
        guess = random.randint(1, 1000000)
        print("Well,", Name, "I am thinking of a number in between 1 and 1000000.")
    while answer != "I QUIT":
            answer = input("Take a guess: ")
            if answer < guess:
                 print("Guess to low")
            if answer > guess:
                 print("Guess to high")
            if answer == guess:
                break

if __name__ == "__main__":
    main()
