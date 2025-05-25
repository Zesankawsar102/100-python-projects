def binary_to_decimal():
    print("🔢 Binary to Decimal Converter")
    binary = input("Enter a binary number (e.g. 1010): ")

    try:
        decimal = int(binary, 2)
        print(f"✅ Decimal value: {decimal}")
    except ValueError:
        print("❌ Invalid binary number. Please use only 0 and 1.")

if __name__ == "__main__":
    while True:
        binary_to_decimal()
        again = input("\nConvert another? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break
