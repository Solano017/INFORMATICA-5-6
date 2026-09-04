import random

def main():
    print("Learning Python")




    answer = ""
    stk=3
    streak = 0
    while streak != stk:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num3 = random.randint(2,5)
        result = num1 + num2
        answer = int(input(f"what is {num1} + {num2}: "))
        if answer < result:
            print("Guess too low")
            streak -= streak
            print(f"INCORRECT, The right answer was: {result}")
            print("You lost your streak")
            print("Current streak:", streak)
        if answer > result:
            print("Guess too high")
            streak -= streak
            print(f"INCORRECT, The right answer was: {result}")
            print("You lost your streak")
            print("Current streak:", streak)

        if answer == result:
            print("Correct!")
            streak += 1
            print("You got a streak of", "🌟"*streak)

        if streak == 3:
            print("You are right, see you really soon")
            break
    print("Aight, long enough")
    print("Exponents, Multiplications, or everything")
    fate = input("Now choose your fate: ")

# Under construction


if __name__ == "__main__":
    main()
