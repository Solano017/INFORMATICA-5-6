def main():
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

if __name__ == "__main__":
        main()
