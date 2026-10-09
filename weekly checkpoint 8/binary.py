def main(): # 2 point
    bnumber = []
    print("Welcome to Binary to Decimal converter!")
    print("""
    The purpose of our program is to help the user
    convert a binary number into a decimal number
    and work as a calculator and apply our current
    knowledge on python to fulfill the user necessity.
    """) # 1 point
    while True:
        bnumber = input("Enter a binary number: ")
        is_valid = True
        if bnumber == "":
            is_valid = False
        else:
            for char in bnumber:
                if char not in ['0', '1']:
                    is_valid = False
                    break

        if is_valid:
            break
        else:
            print("Not valid, enter a valid input")


    binary_to_decimal(bnumber)
def binary_to_decimal(bnumber):
    decimal = 0
    power = len(bnumber) - 1

    for digit in bnumber:
        decimal += int(digit) * (2 ** power)
        power -= 1
    print(f"Answer: {decimal}")

if __name__ == "__main__":
    main()
