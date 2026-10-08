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
        try:
            bnumber = int(input("Enter a binary number: ")) # 1 or 2
            break
        except ValueError:
            print("We need to use numbers")



    binary_to_decimal(bnumber)
def binary_to_decimal(bnumber): #2 point
    print("Now this is your binary number to decimal number")
    num1 = bnumber[0]
    num2 = bnumber[1]
    print(num1)
    print(num2)

if __name__ == "__main__":
    main()
