import cv2
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
import re

#cv2.IMREAD_COLOR : 투명한 부분 무시되는 컬러
#cv2.IMREAD_GRAYSCALE : 흑백 이미지로 로드
#cv2.IMREAD_UNCHANGED : 알파 채널을 포함한 이미지 그대로 로드

# OCR 정확도 개선을 위한 이미지 전처리
image = cv2.imread('banana.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이 스케일로 변환
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # 배경에서 전경 텍스트를 분할하기 위한 임계값 사용, 회색배경 위에 겹쳐진 검은색 텍스트 읽는데 유용

cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
    min_y = int(temp[2])
    max_x = int(temp[3])
    max_y = int(temp[4].replace(";",""))
    coordinates.append((text, min_x, min_y, max_x, max_y))

"""1) 각 줄마다 단어들의 min_x와 max_x의 합이 증가하는 지 확인"""
"""2) 각 줄의 첫번째 단어의 min_y와 max_y의 합이 증가하는 지 확인"""
"""*) 이미지 전처리를 통해 더 정확한 글자 추출이 가능하도록"""

idx = 0
line_x = []
for i in range(len(lines)):
    sum = 0
    for j in range(len(lines[i])):
        sum += coordinates[idx][1] + coordinates[idx][3] # min_x+max_x
        idx += 1
    print(sum)
    line_x.append(sum)
