def main():
    print("WELCOME TO")
    print("TO DO LIST")
    tasks = []
    while True:
        print(f"You have {len(tasks)} tasks to do.")
        print(tasks)
        command = input("What do you want to do? (add, complete, or stop): ").lower()
        if command == "add":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
        elif command == "stop":
            break
    while 


    print(list)

if __name__ == "__main__":
    main()
