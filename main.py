import qrcode
import os

while True:
    # Getting URL from user in this setion
    data = input('Enter any text or URL (or type "exit" to quit): ').strip()
    if data.lower() == "exit":
        print("Exiting the QR code generator.")
        break
    if not data:
        print("Error: Data cannot be empty. Please enter valid input.")
        continue

    
    # Getting File Name from the user in this section
    file_name = input('Enter the file Name (without extension): ').strip()
    if file_name.lower() == "exit":
        print("Exiting the QR code generator.")
        break
    if not file_name:
        print("Error: File name cannot be empty. Please enter a valid name.")
        continue

    
    # Getting Fill-Colour from the user in this section
    color = input('Enter fill color of the QR Code (default: White): ').strip()
    if color.lower() == "exit":
        print("Exiting the QR code generator.")
        break
    if not color:
        color = 'White' #This is the default fill colour of the qrcode 
        
        
    # Initialize QR Code
    qr = qrcode.QRCode(box_size=12, border=1)
    qr.add_data(data)
    
    
    # Generating and save Qr Code image
    try:
        image = qr.make_image(fill_color=color, back_color='Black')
    except ValueError:
        print('Error: Invalid color input. Using default (Black).')
        image = qr.make_image(fill_color='Black', back_color='Black')
        

    # Ensure correct file extension
    file_path = f"{os.path.splitext(file_name)[0]}.jpeg"
    image.save(file_path)


    # Printing Sucesses message
    print(f'✅ QR Code saved as {file_path}\n')

print('Thank you for using my qr-code generator...')