while True: 
    principal = 0
    interest = 0
    time = 0
    number = 0

    while principal <= 0:
        principal = float(input("Enter the amound of principal: "))
        if principal<= 0:
            print("Principal can't be less than or equal to 0.")

    while interest <= 0:
        interest = float(input("Enter the interest per year: "))
        if interest <= 0:
            print("Interest can't be less than or equal to 0.")

    while number <= 0:
        number = int(input("Enter the number of times the interest is compunded per year: "))
        if number <= 0:
            print("Number of times interest compunded can't be less than or equal to 0.")

    while time <= 0:
        time = int(input("Enter the time in year(s): "))
        if time<= 0:
            print("Time can't be less than or equal to 0.")

    amount = principal * (1 +(interest/100)/number) ** (number * time)

    print(f"{amount:.2f}")

    repeat = input("Do you want to repeat the calculations(yes/no): ").lower()
    if repeat != "yes":
        print("Thanks for using the calculator.")
        break