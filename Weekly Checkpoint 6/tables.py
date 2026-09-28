def main():
    table = ""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while table != "exit":
        table = int(input("Multiplication table from 1-10: "))
        if table in numbers:
            for multiplication in numbers:
                if multiplication != "":

                    print(f"{multiplication} times {table} is", multiplication * table)
        elif table not in numbers:
            print("Pick a number from 1 to 10")



if __name__ == "__main__":
    main()
