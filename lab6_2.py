from cv2 import cv2 
from numpy import pi, cos, sin, shape

def draw_line_P(img, x1, y1, x2, y2, color = (255, 255, 255), thickness = 2, lineType=cv2.LINE_AA):
    cv2.line(img, (x1, y1), (x2, y2), color, thickness, lineType)

# 1й Способ: HoughLines() - стандартное преобразование Хафа
img = cv2.imread('6_2.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invers_img_gray = cv2.bitwise_not(img_gray)

edges = cv2.Canny(img_gray, 75, 230)

lines = cv2.HoughLines(image = edges, rho = 1, theta = pi/360, threshold = 150)

for line in lines:
    rho, theta = line[0]
    a = cos(theta)
    b = sin(theta)
    print("a, b: ", a,b)
    x0 = a * rho
    y0 = b * rho
    print("xo, yo: ", x0, y0)
# 1200 - длина линии
    x1 = int(x0 + 1200 * (-b))
    y1 = int(y0 + 1200 * (a))

    x2 = int(x0 - 1200 * (-b))
    y2 = int(y0 - 1200 * (a))

    cv2.line(img = img, pt1 = (x1, y1), pt2 = (x2, y2), color = (255, 255, 255), thickness = 15)

cv2.imshow('Edges', edges)
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()

# 2й способ: HoughLinesP() - прогрессивное вероятностное преобразование Хафа
img_orig = cv2.imread('6_2.png')
img_gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
img_result = img_orig.copy()

_, thresh = cv2.threshold(img_gray, 125, 255 , cv2.THRESH_BINARY_INV) 

lines = cv2.HoughLinesP( image = thresh, rho = 1, theta = pi/180, threshold = 255, maxLineGap = 15)

print(shape(lines))

for line in lines:
    print(line)
    x1 , y1 , x2 , y2 = line[0]
    draw_line_P(img_result, x1 , y1 ,x2, y2)

cv2.imshow('Original image', img_orig)
cv2.imshow('Without lines', img_result)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()