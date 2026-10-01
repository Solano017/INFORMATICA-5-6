import random

def main():
    coin = ["heads", "tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choice(coin)
        guess = input("Heads or tails? ").strip().lower()

        print("The coin landed on", flip)

        if guess == flip:
            print("You won!")
            break
        else:
            print("You lost")
            attempts -= 1
            print("Attemps left:", attempts)

if __name__ == "__main__":
    main()
