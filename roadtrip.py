def main():
    answer = "" # Initialize

    while answer != "Yes!": # Condition
        answer = input("Are we there yet? ").strip().title() # Update
        if answer == "Yes":
            followup = input("Really? ").strip().title()
        if followup == "Yes!":
            break
    print("We just arrived")


if __name__ == "__main__":
    main()
