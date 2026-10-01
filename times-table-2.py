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

                    else:
                        print(f"{x} times {times_table} is {answer}")
                        print("Incorrect")
                except ValueError:
                    print("Invalid")
            break

    else:
        print("Times Table has to be between 1 to 10, not higher nor lower.")
        print("Try again pls")


if __name__ == "__main__":
    main()
