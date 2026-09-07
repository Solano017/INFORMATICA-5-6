import random
def main():

    print("================================")
    print("     DID I PACK EVERYTHING?     ")
    print("================================")

    items = ["Phone", "Backpack", "Homework", "Water", "Keys"]
    packed = []

    print()
    print("You are getting ready to leave!")
    print("Let's make sure you have everything.")
    print()


    while len(packed) < len(items):
        print("Items you still need:")
        for item in items:
            if item not in packed:
                print("- ", item)
        print()

        choice = input("What did you pack? ").strip().title()

        if choice in items and choice not in packed:
            packed.append(choice)
            print("✅", choice, "is packed!")
        elif choice in packed:
            print("⚠️ You already packed that!")
        else:
            print("❌ That's not on your list.")
        print()

    print("================================")
    print("🎉 EVERYTHING IS PACKED!")
    print("You're ready to go!")
    print("================================")


if __name__ == "__main__":
    main()
