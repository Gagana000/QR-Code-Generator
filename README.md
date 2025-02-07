# QR Code Generator  

A simple Python program to generate QR codes from text or URLs. This script lets users create QR codes with custom colors and save them as image files.  

## Features  

✅ Accepts any text or URL input  
✅ Customizable QR code color  
✅ Saves the generated QR code as a `.jpeg` file  
### Importent 
gagana.jpeg 
rantharu.jpeg Files are test files

## Installation  

Make sure you have Python installed, then install the required library:  

```bash
pip install qrcode[pil]
```

## Usage  

Run the script and follow the prompts:  

```bash
python qr_code_generator.py
```

You'll be asked to enter the text or URL for the QR code and provide a filename for saving the image. The QR code will be generated and saved in the current directory.  

## Example  

```
Enter any text or URL: https://github.com/your-repo  
Enter the file Name: my_qr_code  
QR Code Saved as my_qr_code.jpeg  
```

## Dependencies  

- `qrcode` (for generating QR codes)  
- `PIL` (for image processing, included in `qrcode[pil]`)  

## Contribution  

Feel free to fork this repository and improve the script. Pull requests are welcome!  

## License  

This project is open-source under the MIT License.

