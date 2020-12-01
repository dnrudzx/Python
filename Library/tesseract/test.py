from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr():
    file = '캡처.PNG'
    image = Image.open(file)
    text = image_to_string(image, lang='kor')
    print(text)

ocr()
