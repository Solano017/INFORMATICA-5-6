def main():
    transitors = 17.8
    years = int(input("How many years into the future do you want to calculate: "))
    current_year = 2026
    if(current_year + years) >= 2030:
        print("The law is not valid.")
    else:
        transitors *= 2 ** (years/2)
        print(transitors, "Billions")

    print("Transitors quantity is on billions")
if __name__ == "__main__":
    main()
