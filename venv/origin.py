import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
import re

#print(pytesseract.image_to_boxes('banana.jpeg'))
output = pytesseract.image_to_string('banana.jpeg')
#print(output)

lines = []
sentence = output.split('\n')
for line in sentence:
    if not line: continue
    #print(line.split())
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

idx = 0
line_sum = []
for i in range(len(lines)):
    sum = 0
    for j in range(len(lines[i])):
        sum += coordinates[idx][1]+coordinates[idx][2]+coordinates[idx][3]+coordinates[idx][4] # min_x+min_y+max_x+max_y
        idx += 1
    print(sum)
    line_sum.append(sum)

"""
증가한다고 판단하는 기준?
증가하는 구간 >= 감소하는 구간?
"""

increase=0
decrease=0
for i in range(len(line_sum)-1):
    if(line_sum[i] <= line_sum[i+1]): increase+=1
    else: decrease+=1

if(increase>=decrease): print("정상")
else: print("비정상")