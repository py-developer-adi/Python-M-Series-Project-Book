'''PYCODE | @_py.code'''

# ? 9. QR Code Generator/Reader
# ? Features: Generate and read QR codes.

# * Source Code
import qrcode
import cv2

def display_menu():
    print("\n--- QR Code Generator and Reader ---")
    print("1. Generate QR Code")
    print("2. Read QR Code")
    print("3. Exit")

def generate_qr_code():
    data = input("Enter the data to encode in the QR Code: ")
    filename = input("Enter the filename to save the QR Code (e.g., 'qrcode.png'): ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR Code saved as {filename}")
    img.show()

def read_qr_code():
    filename = input("Enter the filename of the QR Code to read (e.g., 'qrcode.png'): ")
    try:
        # Open the image using OpenCV
        image = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        data, points, _ = detector.detectAndDecode(image)

        if points is not None:
            print(f"Data in QR Code: {data}")
        else:
            print("No QR Code detected in the image.")
    except Exception as e:
        print(f"Error reading QR Code: {e}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            generate_qr_code()
        elif choice == '2':
            read_qr_code()
        elif choice == '3':
            print("Exiting QR Code Generator and Reader. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
