def main():
    nums = []
    for i in range(1,11):
        nums.append(str(i))
    while True:
        times_table = input("Enter a number 1-10: ")
        if times_table == "exit":
            break
        elif times_table in nums:
            print(f"Here is the {times_table} times table")
            for x in range(1,11):
                result = int(times_table) * x
                print(f"{x} times {times_table} is {result}")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
