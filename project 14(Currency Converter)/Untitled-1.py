def usd_to_bdt():
    rate = 110.5  # Example rate, update as needed
    try:
        usd = float(input("Enter amount in USD: "))
        bdt = usd * rate
        print(f"{usd} USD = {bdt:.2f} BDT")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    usd_to_bdt()
