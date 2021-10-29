import pytesseract
from cv2 import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = r'D:\Python\TextReader\tur(2)_text.png'
img = cv2.imread(path)
cv2.imshow('img', img)
cv2.waitKey(0)
result = pytesseract.image_to_string(img, lang='tur')
# text_file = open(r"TextReader\Result.txt", "w+")
# text_file.write(result)
# text_file.close()
with open(r'TextReader\Result.txt', 'w') as file:
    file.write(result[:-1])
# cv2.imshow('Result' , img)
# cv2.waitKey(0)