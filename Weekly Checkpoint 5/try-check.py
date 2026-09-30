def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Must enter a Number")
if __name__ == "__main__":
    main()
