def main():

    rating = float(input("Rate your food on a scale from 0-5 stars: "))

        # Rating limits:  must be in betwen the asked quantity
    if rating > 5:
        print("Rating must be on a scale from 0-5")
    elif rating < 0:
        print("Rating cant be below 0")
        # Ratings: Rate
    elif rating >= 4.5:
        print("Perfection")
    elif rating >= 4:
        print("Excellent")
    elif rating >= 3:
        print("Good")
    elif rating >= 2:
        print("Fair")
    else:
        print("Poor.")
    print("See you soon")
if __name__ == "__main__":
    main()
