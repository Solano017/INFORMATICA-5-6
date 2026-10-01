def main():
    spain = int(input("Spain goals: "))
    argentina = int(input("Argentina goals: "))

    if spain > argentina:
        print("Spain is the winner")
    elif spain < argentina:
        print("Argentina is the winner")
    else:
        print("Its a tie.")
    print("GG.")
if __name__ == "__main__":
    main()
