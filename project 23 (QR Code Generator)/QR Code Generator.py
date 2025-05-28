import qrcode

def generate_qr():
    data = input("Enter the text or URL to encode: ").strip()
    filename = input("Enter filename (without .png): ").strip()

    if not data or not filename:
        print("❌ Data or filename cannot be empty.")
        return

    # Create QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")

    print(f"✅ QR Code successfully saved as {filename}.png")

if __name__ == "__main__":
    generate_qr()
