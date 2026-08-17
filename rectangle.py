def main():
    width = int(input("Enter the width of the rectangle: "))
    print("o" * width)
    print("o" * width)
    print("o" * width)
    print("o" * width)
    print("o" * width)
    Perimeter = 2 * width + 10
    print("Your perimeter is", Perimeter)
    Diagonal = ((5 ** 2)/5 + (width ** 2)/ width)
    print("Diagonal:", Diagonal)

    word = input("Enter the word to repeat: ")
    times = int(input("Enter the times to repeat the word: "))
    print(word * times)
if __name__ == "__main__":
    main()
