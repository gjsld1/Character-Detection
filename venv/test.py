import cv2


#cv2.IMREAD_COLOR : 투명한 부분 무시되는 컬
#cv2.IMREAD_GRAYSCALE : 흑백 이미지로 로
#cv2.IMREAD_UNCHANGED : 알파 채컬을 포함한 이미지 그대로 로드
src = cv2.imread('ginja.png', cv2.IMREAD_COLOR)
dst = cv2.imread(src, cv2.COLOR_BGR2GRAY)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()