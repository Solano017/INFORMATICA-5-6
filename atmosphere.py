def main():

    atmosphere = input("Descent atmosphere layer: ")
    if atmosphere == "Exosphere":
        a1 = 700
        a2 = 10000
        v = 
    elif atmosphere == "Thermosphere":
        a1 = 85
        a2 = 700
        v =
    elif atmosphere == "Mesosphere":
        a1 = 50
        a2 = 85
        v =
    elif atmosphere == "Stratosphere":
        a1 = 12
        a2 = 50
        v =
    elif atmosphere == "Troposphere":
        a1 = 0
        a2 = 12
        v =
    else:
        print ("Invalid Option")
    print("Your altitude level will be between", a1, "and", a2, "km")
    altitude = float(input("Enter exact altitude: "))
    if altitude <= (a1 - 1):
        print("Invalid")
    elif altitude >= (a2 +1):
        print("invalid")
    print(altitude)

if __name__ == "__main__":
    main()
