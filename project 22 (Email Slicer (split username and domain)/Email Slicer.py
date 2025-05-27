def email_slicer():
    print("✂️ Email Slicer Tool\n")
    email = input("Enter your email address: ").strip()

    if "@" in email:
        username, domain = email.split("@", 1)
        print(f"🧑 Username: {username}")
        print(f"🌍 Domain: {domain}")
    else:
        print("❌ Invalid email format. Please include '@'.")

if __name__ == "__main__":
    while True:
        email_slicer()
        again = input("\nSlice another? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break
