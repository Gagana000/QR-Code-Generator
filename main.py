import qrcode

data = input('Enter any text or URL : ').strip()
file_name = input('Enter the file Name : ').strip()
qr = qrcode.QRCode(box_size=12, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='green', back_color='Black')
image.save(file_name + '.jpeg')

print(f'QR Code Saved as {file_name}')