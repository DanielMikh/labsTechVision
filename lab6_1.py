from cv2 import cv2
import numpy as np
from math import sqrt

def draw_line_P(img, x1, y1, x2, y2, color = (0, 0, 255), thickness = 2, lineType=cv2.LINE_AA):
    cv2.line(img, (x1, y1), (x2, y2), color, thickness, lineType)

def draw_circle(img, center, radius, color=(255, 0, ), thickness = 2, lineType = cv2.LINE_AA):
    cv2.circle(img, center, radius, color, thickness, lineType)

# Получим изображение
img = cv2.imread('6_1.png')
# Переменные для вывода результата в разных окнах cv2.imshow()
lines_img = np.copy(img)
longestLine_img = np.copy(img)
circles_img = np.copy(img)
biggestCircle_img = np.copy(img)

# Получим полутоновое изображние
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invers_img_gray = cv2.bitwise_not(img_gray)

# При таких значениях аргументов функции на изображении выделяются только линии
lines = cv2.HoughLinesP(invers_img_gray, rho = 1, theta = np.pi/720, threshold = 255, maxLineGap = 15)

print("Lines: ", lines)
maxLength = 0
x_1, y_1, x_2, y_2 = 0, 0, 0, 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    print("x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}".format(x1 = x1, x2 = x2, y1 = y1, y2 = y2))

    currentLength = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print('CurrentLenght: ', currentLength, '\n')

    if currentLength >= maxLength:
        maxLength = currentLength
        x_1, y_1, x_2, y_2 = x1, y1, x2, y2
        
    draw_line_P(lines_img, x1, y1, x2, y2)

draw_line_P(longestLine_img, x_1, y_1, x_2, y_2)

edges = cv2.Canny(img_gray, 75, 255)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp = 1, minDist = 280, 
                                param1 = 255, param2 = 97, minRadius = 0, maxRadius = 0)
print("Circles: ", circles)                               

# Координаты и радиус для самой большой окружности
x_max, y_max, r_max = 0, 0, 0
# Выделим все найденные окружности
for circle in circles[0]:
    x0, y0, r = circle
    print(x0,y0,r)

    if r > r_max:
        x_max, y_max, r_max = x0, y0, r

    draw_circle(circles_img, (x0, y0), r)
# Выделим самую большую окружность
draw_circle(biggestCircle_img, (x_max, y_max), r_max)


cv2.imshow('All lines', lines_img)
cv2.imshow('Longest line', longestLine_img)
cv2.imshow('Circles', circles_img)
cv2.imshow('Biggest circle', biggestCircle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()