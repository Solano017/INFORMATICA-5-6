def main():
    # Easy Calculator
        number1 = int(input("Give me a number: "))
        if number1 >= 0:
            print(number1)
        elif number1 <= 0:
            print(number1 * -1)
    # Medium Calculator
        print("Calculator Medium")
        number2 = int(input("Give me a number: "))
        number3 = int(input("Give me a number: "))
        print("1 = Add")
        print("2 = Substract")
        print("3 = Multiply")
        print("4 = Divide")
        operation = int(input("What operation do you want to perform: "))
        if operation == 1:
            answer = number2 + number3
            print("Here is your result", answer)
        elif operation == 2:
            answer = number2 - number3
            print("Here is your result", answer)
        elif operation == 3:
            answer = number2 * number3
            print("Here is your result", answer)
        elif operation == 4:
            answer = number2 / number3
            print("Here is your result", answer)
        else:
            print("Invalid Operation")



if __name__ == "__main__":
    main()
