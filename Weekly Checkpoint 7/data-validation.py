def main():
            # Number Code

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number in nums:
                print("Number stored succesfully.")
                not_validated = False # break
            else:
                 print("Not in berween 1 and 10")
        except ValueError:
             print("Enter a Number")

                # Name code

    while True:
        try:
            name = input("Enter your name: ")
            f_letter = name[0]
            print("Name stored succesfully.")
            break
        except IndexError:
            print("Bruh")
            print("A name is required")

    name = 0
    while name != "":
        name = input("Enter your name: ")
        if name == "":
            print("A name is required.")
            name = 0
        else:
            print("Name has been stored")
            break


if __name__ == "__main__":
        main()
