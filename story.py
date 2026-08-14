def main():
    # planet = input("Planet: ")

    # # Separation
    # print("Hello", planet)

    # #Ending
    # print("Hello", end =" ")
    # print(planet)

    # # Concatenation
    # print("Hello " + planet)

    # #Formated String
    # print(f"Hello {planet}") ctrl k c = comment



    name = input("What´s your name? ").title().strip()
    color = input("Tell me a color: ").lower().strip()
    adj = input("Tell me an adjetive: ").lower().strip()
    goal = input("A goal you would like to achieve: ").lower().strip()

    print("Hello", name)
    print(" ")
    print("This is your story")
    print(f"At dawn the sky turned {color}, and the air fel {adj}. I decided today I will finally {goal}.")
    print(f"At dawn the sky turned {color}, and the air fel {adj}. I decided today I will finally {goal}.".upper())

if __name__ == "__main__":
    main()
