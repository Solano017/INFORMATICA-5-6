def main():
    print("Welcome")

    valid_bits = ["0", "1"]
    while True:
        correct_chars = 0
        binary_number = input("Enter your binary number: ")
        for char in binary_number:
            if char in valid_bits:
                correct_chars += 1
        if correct_chars == len(binary_number):
            break
        else:
            print("Invalid input")

    binary_to_decimal(binary_number)
def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = (decimal * 2) + int(bit)
    print(decimal)

if __name__ == "__main__":
    main()
