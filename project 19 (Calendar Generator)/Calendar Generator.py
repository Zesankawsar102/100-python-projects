import calendar

def generate_calendar():
    print("Welcome to Calendar Generator!\n")
    try:
        year = int(input("Enter the year (e.g. 2025): "))
        month = int(input("Enter the month (1-12): "))

        if 1 <= month <= 12:
            print(f"\n📅 Calendar for {calendar.month_name[month]} {year}:\n")
            print(calendar.month(year, month))
        else:
            print("Month must be between 1 and 12.")
    except ValueError:
        print("Please enter valid numeric input.")

if __name__ == "__main__":
    generate_calendar()
