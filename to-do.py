def main():
    print("WELCOME TO")
    print("TO DO LIST")
    tasks = []
    while True:
        print(f"You have {len(tasks)} tasks to do.")
        t = len(tasks)
        if t == 0:
            print("Waiting for tasks :)")
        else:
            print(tasks)
        command = input("What do you want to do? (add, check, complete, or exit): ").lower()
        if command == "add":
            new_task = input("Enter a new task: ").lower()

            if new_task not in tasks:
                tasks.append(new_task)
            elif new_task in tasks:
                del_confirm = input(f"Did you complete {new_task}? (y/n))
                
        elif command == "check":
            check = input("Task to complete: ").lower()
            tasks.remove(check)
        elif command == "exit":
            break
        else:
            continue


    print("Thank you for using, see you later")

if __name__ == "__main__":
    main()
