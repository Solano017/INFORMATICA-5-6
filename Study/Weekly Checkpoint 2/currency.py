def main():
    co = float(input("What do you have left in colombian pesos?: "))
    pe = float(input("What do you have left in soles?: "))
    br = float(input("What do you have left in reals: "))
    colombian = co * 0.0054
    peruvian = pe * 5.06
    brazilian = br * 3.28
    usd = 17.06
    totalmx = round(colombian + peruvian + brazilian)
    totalusd = round(totalmx / usd)
    print("This is your total in MX:", totalmx)
    print("This is your total in USD:", totalusd)
if __name__ == "__main__":

    main()
