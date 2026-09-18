def main():
    print("WELCOME TO YOUR TO DO LIST")
    tasks = []

    while True:
        print(f"You have {len(tasks)} tasks to do.")

        if len(tasks) == 0:
            print("Waiting for tasks :)")
        else:
            print(tasks)

        command = input("What do you want to do? (add, remove, or exit): ").lower()

        if command == "add":
            new_task = input("Enter a new task: ").lower()
            tasks.append(new_task)

        elif command == "remove":
            new_task = input("Task to remove: ").lower()
        elif command == "exit":
            break
        if new_task in tasks:
            new_task(task)
            print("Task removed!")
        else:
            print("That task is not on your list.")


    print("Thank you for using, see you later")


if __name__ == "__main__":
    main()
