import qrcode


to_qr = input("Enter website/text that you would like to create a QR code for: ")
file_name = input("Enter name for your qr code file: ")
try:
    img = qrcode.make(to_qr)
    img.save(f"{file_name}.png")
    print("QR code created successfully")
except Exception as e:
    print(f"Error: {e}")




