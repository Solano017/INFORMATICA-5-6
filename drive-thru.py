def main():
    welcome()
    choice = int(input("Select your order: "))
    get_item(choice)


def welcome():
    menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
    print("Welcome to dashbus!")
    print("Here is the menu:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")
def get_item(order):
    sticker = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    try:
        print(sticker[order - 1])
    except IndexError:
        print("Not in our menu")
    except ValueError:
        print("Not a number")
    #if order == 1:
        #print("🍔")


if __name__ == "__main__":
    main()
