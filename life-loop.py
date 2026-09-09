import random
import time
def main():

    print("================================")
    print("     DID I PACK EVERYTHING?     ")
    print("================================")

    items = ["Phone", "Backpack", "Homework", "Water", "Keys"]
    packed = [""]

    print()
    print("You are getting ready to leave!")
    print("Let's make sure you have everything.")
    print()

    phone = "no"
    backpack = "no"
    homework = "no"
    water = "no"
    keys = "no"

    packed = 0

    while packed != 5:

        print("Items you still need:")
        if phone == "no":
            print("--phone")
        if backpack == "no":
            print("--backpack")
        if homework == "no":
            print("--homework")
        if water == "no":
            print("--water")
        if keys == "no":
            print("--keys")

        print("")

        choice = input("What did you pack? ").strip().title()
        if choice == "Phone":
            if phone == "no":
                phone = "yes"
                packed = packed + 1
                print("Phone Packed")
            else:
                print("Phone is already packed")
        elif choice == "Backpack":
            if backpack == "no":
                backpack == "yes"
                packed = packed + 1
                print("Backpack is packed")
            else:
                print("Backpack is already packed")
        elif choice == "Homework":
            if homework == "no":
                homework = "yes"
                packed = packed + 1
                print("Homework is packed")
            else:
                print("Homework is already packed")
        elif choice == "Water":
            if water == "no":
                backpack = "yes"
                packed = packed + 1
                print("Water is packed")
            else:
                print("Backpack is already packed")
        elif choice == "Keys":
            if keys == "no":
                keys = "yes"
                packed = packed + 1
                print("keys are packed")
            else:
                print("Keys are already packed")
        elif choice == "":
            print("Please enter an item name.")
        else:
            print("That is not on yor list")
        if packed == 5:
            break
    print(" ")

    print("Checking your backpack...")
    time.sleep(2)

    print("Almost ready...")
    time.sleep(2)

    print("================================")
    print("🎉 EVERYTHING IS PACKED!")
    print("You're ready to go!")
    print("================================")


if __name__ == "__main__":
    main()
