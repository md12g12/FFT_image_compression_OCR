import cv2
import pytesseract
import numpy as np
import difflib

#install Tesseract from here: https://github.com/UB-Mannheim/tesseract/wiki
#https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def OCR(image):

    #kernel = np.ones((2, 1), np.uint8)
    #img = cv2.erode(image, kernel, iterations=1)
    #img = cv2.dilate(img, kernel, iterations=1)
    out_below = pytesseract.image_to_string(image)
    return(out_below)

def OCR_accuracy(answer, test_string):
    ratio = difflib.SequenceMatcher(None, answer, test_string).ratio()
    return(ratio)

if __name__ == '__main__':
    print(OCR_accuracy(str(OCR("text.png")), str(OCR("text.png"))))
