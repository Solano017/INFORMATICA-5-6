import random

def main():
    coin = random.randint(1, 2)
    if coin == 1:
        coinflip = "HEADS"
    elif coin == 2:
        coinflip = "TAILS"
    user = input(f"Guess: ").upper().strip()
    print(coinflip)
    if user == coinflip:
        print("WINNER")
    else:
        print("LOSER")
if __name__ == "__main__":
    main()
