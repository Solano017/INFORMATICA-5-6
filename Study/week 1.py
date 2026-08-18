def main():
    message = input("Make your word to be randomized: ")

    message = message.replace("A", "Q").replace("B", "M").replace("C", "X").replace("D", "K").replace("E", "P").replace("F", "Z").replace("G", "R").replace("H", "T").replace("I", "L").replace("J", "V").replace("K", "N").replace("L", "A").replace("M", "W").replace("N", "D").replace("O", "Y").replace("P", "F").replace("Q", "S").replace("R", "G").replace("S", "B").replace("T", "H").replace("U", "J").replace("V", "C").replace("W", "E").replace("X", "I").replace("Y", "O").replace("Z", "U")

    print(message)


if __name__ == "__main__":
    main()
