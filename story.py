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

    color2 = input("Tell me a color: ").upper().strip()
    adj2 = input("Tell me an adjetive: ").upper().strip()
    goal2 = input("A goal you would like to achieve: ").upper().strip()

    print("Hello", name)
    print(" ")
    print("This is your story")
    print(f"At dawn the sky turned {color2}, and the air fel {adj2}. I decided today I will finally {goal2}.")

if __name__ == "__main__":
    main()
