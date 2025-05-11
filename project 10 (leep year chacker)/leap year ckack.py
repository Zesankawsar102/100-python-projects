def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

while True:
    try:
        year = int(input("Enter a year (Ctrl+C to exit): "))
        if is_leap_year(year):
            print(f"{year} is a leap year.\n")
        else:
            print(f"{year} is not a leap year.\n")
    except ValueError:
        print("Please enter a valid number.\n")
    except KeyboardInterrupt:
        print("\nProgram was stopped by the user.")
        break
