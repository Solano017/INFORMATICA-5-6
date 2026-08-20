def main():
    #Division
    x = 10
    y = 3

    # 1st. <<Regular Division (x/y)
    print("Regular division:", x / y)

    # 2nd. Floor Division (//)
    print("Floor Division", x // y)

    # 3rd. Remainder Division (//)
    print("Remainder Division", x % y)

    # 4. Division with variables
    pieces = 20
    persons = 5
    result = pieces / persons

    print("divided by 5 =", result)
# inputs
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("Division", a / b)
    print("Whole number division:", a // b)
    print("Remainder:", a % b)

if __name__ == "__main__":
    main()

