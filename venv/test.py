import cv2
import pytesseract
from PIL import Image

from bs4 import BeautifulSoup
import re

#cv2.IMREAD_COLOR : 투명한 부분 무시되는 컬러
#cv2.IMREAD_GRAYSCALE : 흑백 이미지로 로드
#cv2.IMREAD_UNCHANGED : 알파 채널을 포함한 이미지 그대로 로드

#print(pytesseract.image_to_boxes('banana.jpeg'))
output = pytesseract.image_to_string('banana.jpeg')
#print(output)

lines = []
sentence = output.split('\n')

for line in sentence:
    if not line: continue
    print(line.split())
    lines.append(line.split())

hocr = pytesseract.image_to_pdf_or_hocr('banana.jpeg', extension='hocr')

soup = BeautifulSoup(hocr, 'html.parser')
#print(soup)

ocrx_word = soup.select('span.ocrx_word')
#print(ocrx_word)

coordinates = []
for word in ocrx_word:
    #print(word)
    text = word.text
    temp = word.attrs['title'].split()
    min_x = int(temp[1])
    max_x = int(temp[3])
    coordinates.append((text, min_x, max_x))

idx = 0
line_x = []
for i in range(len(lines)):
    sum = 0
    for j in range(len(lines[i])):
        sum += coordinates[idx][1] + coordinates[idx][2]
        idx += 1
    print(sum)
    line_x.append(sum)


"""
print(pytesseract.image_to_string(Image.open('banana.jpeg')))

src = cv2.imread('ginja.png', cv2.IMREAD_COLOR)
src2 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('src2', src2)
dst = cv2.imread(src, cv2.COLOR_BGR2GRAY)

cv2.imshow('src', src)
#cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""