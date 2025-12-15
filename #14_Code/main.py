import qrcode


data = input("Enter text or link for QR Code: ")


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save("my_qr_code.png")

print("✅ QR Code generated successfully as my_qr_code.png")
