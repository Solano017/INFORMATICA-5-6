def main():
    print("Binary to Decimal Converter")
    print("""
    The purpose of our program is to help the user
    convert a binary number into a decimal number
    and work as a calculator and apply our current
    knowledge on python to fulfill the user necessity.
    """)
    
    # Handle unexpected inputs (letters, empty spaces, or numbers other than 0 and 1)
    while True:
        bnumber = input("Enter a binary number: ")
        
        # Validate that it only contains '0' and '1' and is not empty
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
            print("Invalid input. Please enter a valid binary number (only 0s and 1s).")

    # Call the function with the user's input as an argument
    binary_to_decimal(bnumber)

def binary_to_decimal(bnumber):
    # Conversion logic using powers of 2
    decimal = 0
    power = len(bnumber) - 1
    
    for digit in bnumber:
        decimal += int(digit) * (2 ** power)
        power -= 1
        
    print(f"Decimal number: {decimal}")

if __name__ == "__main__":
    main()
