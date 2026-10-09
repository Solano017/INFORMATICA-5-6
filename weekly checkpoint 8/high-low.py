def main():

    num1 = int(input("Pick number 1: "))
    num2 = int(input("Pick number 2: "))
    def highest(a, b):

        if a < b:
            highest_num = b
        else:
            highest_num = a

        print(f"The highest number entered is {highest_num}")
    highest(num1, num2)

    num3 = int(input("Pick number 1: "))
    num4 = int(input("Pick number 2: "))
    num5 = int(input("Pick number 3: "))
    def lowest(c, d, e):

        if e < d and c:
            lowest_num = e
        elif d < c and e:
            lowest_num = d
        else:
            lowest_num = c
        print(f"The lowest number entered is {lowest_num}")

    lowest(num3, num4, num5)
if __name__ == "__main__":
    main()
