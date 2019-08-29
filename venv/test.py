import cv2
import pytesseract
from PIL import Image

from bs4 import BeautifulSoup
import re

#cv2.IMREAD_COLOR : 투명한 부분 무시되는 컬러
#cv2.IMREAD_GRAYSCALE : 흑백 이미지로 로드
#cv2.IMREAD_UNCHANGED : 알파 채널을 포함한 이미지 그대로 로드

#print(pytesseract.image_to_boxes('banana.jpeg'))
hocr = pytesseract.image_to_pdf_or_hocr('banana.jpeg', extension='hocr')

soup = BeautifulSoup(hocr, 'html.parser')
#print(soup)

ocrx_word = soup.select('span.ocrx_word')
#print(ocrx_word)

coordinates = []
for word in ocrx_word:
    #print(word)
    temp = word.attrs['title'].split()
    min_x = int(temp[1])
    min_y = int(temp[2])
    max_x = int(temp[3])
    max_y = int(re.sub(';','', temp[4]))
    print(min_x, min_y, max_x, max_y)
    coordinates.append((min_x, min_y, max_x, max_y))

line_x = []
for i in range(len(max_x)):
    if(i==0): temp=max_x[i]
    elif(max_x[i]==max_x[i-1]):
        temp += max_x[i]
        flag=1
    else: temp=max_x[i]

    if(flag==1): continue
    else: line_x.append(temp)
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