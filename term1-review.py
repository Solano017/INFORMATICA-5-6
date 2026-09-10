from datetime import datetime
def main():

    day = datetime.now().weekday()
    #day = int(input("What day is it today? "))
    days = ["Monday", "Tuesday",
            "Wednesday", "Thursday",
            "Friday", "Saturday",
            "Sunday"]
    print(days[day])
    if day < 4:
        print("Its a Weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("Its friday")
        print("Just a day left until the weekend")
    else:
        print("Its the Weekend!!!")
    months = ["January", "February",
              "March", "April", "May",
              "June", "July", "August",
              "September", "October", "November",
              "December"]
    print("These are the summer months")
    print("-",months[5])
    print("-",months[6])
    print("-",months[7])
    month = datetime.now().month
    print("It is", months[month-1])
if __name__ == "__main__":
    main()
