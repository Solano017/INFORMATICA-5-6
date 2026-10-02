def main():
    print("-----------Hakoot-----------")
    print("Welcome to: Times Table Quiz")
    trye = 0
    while trye == 0:
        while True:
            try:
                times_table = int(input("Enter a times table you would like to get tested from 1 to 10: "))
                if 1 >= times_table >= 10:
                    print("not a number in between")
                elif 1 <= times_table <= 10:

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

        print(f"Here is your quiz on the {times_table} times table")
        while True:
            for x in range(1, max_value):
                while True:
                    try:
                        answer = x * times_table
                        print(f"{times_table} times {x} is equal to?")
                        user_answer = int(input("Answer: "))
                        if user_answer == answer:
                            print(f"{times_table} times {x} is {answer}")
                            print("Correct")
                            score += 1
                            print(f"actual score is: {score} / {max_value - 1}")
                            break
                        else:
                            print(f"{times_table} times {x} is {answer}")
                            print("Incorrect")
                            print(f"actual score is: {score} / {max_value - 1}")
                            break
                    except ValueError:
                        print("Invalid")
            break
        trye += 1


    print("See you later, gg")


if __name__ == "__main__":
    main()
