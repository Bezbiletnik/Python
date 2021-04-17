import pytesseract
from cv2 import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = r'D:\Programing\TextReader\Text(2).jpg'
img = cv2.imread(path)
result = pytesseract.image_to_string(img)
# text_file = open(r"TextReader\Result.txt", "w+")
# text_file.write(result)
# text_file.close()
with open(r'TextReader\Result.txt', 'w') as file:
    file.write(result)
# cv2.imshow('Result' , img)
# cv2.waitKey(0)