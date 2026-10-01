def main():

    atmosphere = input("Descent atmosphere layer: ")
    if atmosphere == "Exosphere":
        a1 = 700
        a2 = 10000
        v = 2000
    elif atmosphere == "Thermosphere":
        a1 = 85
        a2 = 700
        v = 2000
    elif atmosphere == "Mesosphere":
        a1 = 50
        a2 = 85
        v = 2000
    elif atmosphere == "Stratosphere":
        a1 = 12
        a2 = 50
        v = 2000
    elif atmosphere == "Troposphere":
        a1 = 0
        a2 = 12
        v = 2000
    else:
        print ("Invalid Option")
    print("Your altitude level will be between", a1, "and", a2, "km")
    d = float(input("Enter exact altitude: "))
    if d <= (a1 - 1):
        print("Invalid")
    elif d >= (a2 +1):
        print("invalid")
    Te = 615 / 0.05
    M = 35 / 0.2
    S = 38 / 0.075
    Tr = 12 / 0.02
    if a1== 700:
        ft = Te + M + S + Tr
        dt = (d- 700) / 2
    if a1== 85:
        ft = M + S + Tr
        dt = (d-85) / 0.5
    if a1 == 50:
        ft = S + Tr
        dt = (d-50) / 0.2
    if a1 == 12:
        ft = Tr
        dt = (d-12) / 0.075
    if a1 == 0:
        ft = 0
        dt = (d-0) / 0.02
    else:
        ft = 0
    answer = ft + dt
    print("Descent time:", answer)
if __name__ == "__main__":
    main()
