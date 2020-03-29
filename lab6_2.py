from cv2 import cv2
import numpy as np

def draw_line_P(img, x1, y1, x2, y2, color = (255, 255, 255), thickness = 2, lineType=cv2.LINE_AA):
    cv2.line(img, (x1, y1), (x2, y2), color, thickness, lineType)

img_orig = cv2.imread('6_2.png')
img_gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
img_result = img_orig.copy()

_, thresh = cv2.threshold(img_gray, 125, 255 , cv2.THRESH_BINARY_INV) 

lines = cv2.HoughLinesP( image = thresh, rho = 1, theta = np.pi/180, threshold = 255, maxLineGap = 15)

print(np.shape(lines))

for line in lines:
    print(line)
    x1 , y1 , x2 , y2 = line[0]
    draw_line_P(img_result, x1 , y1 ,x2, y2)

cv2.imshow('Original image', img_orig)
cv2.imshow('Without lines', img_result)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()