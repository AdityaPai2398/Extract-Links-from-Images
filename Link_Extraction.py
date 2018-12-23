from PIL import Image
import pytesseract
import cv2
import re
import os
import webbrowser

img=cv2.imread("Testing.png")

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

file="{}.png" .format(os.getpid())
cv2.imwrite(file,gray)

text=pytesseract.image_to_string(Image.open(file))
os.remove(file)

print(text)


urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print(urls[0])

webbrowser.open(urls[0])

