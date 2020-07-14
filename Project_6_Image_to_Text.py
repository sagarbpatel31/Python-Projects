import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r"D:\College\OTHERS\Udemy\Python 20plus projects Arbaz\Tesseract-OCR\tesseract.exe"

def convert():
    im=Image.open('img.png')
    text=pytesseract.image_to_string(im)
    print(text)

print("Image to Text Conversion")
print()

convert()