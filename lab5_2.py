from cv2 import cv2
from math import pi
img = cv2.imread('open-logo.png')
img_gray = cv2.imread('open-logo.png', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

"""
Contours это список всех контуров изображения, каждый контур это Numpy array, 
где (x,y) координаты граничных точек объекта
"""
contours1, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Количество контуров функции threshold():' + str(len(contours1)))


blur = cv2.GaussianBlur(img_gray,(1,1), cv2.BORDER_DEFAULT)
canny = cv2.Canny(image = blur, threshold1 = 200, threshold2 = 225, apertureSize = 3, L2gradient = True)

contours2, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Количество контуров функции Canny():' + str(len(contours2)) + '\n')

# Выделим все контуры цветом на исходном изображении
cv2.drawContours(img, contours2, -1, (25, 150, 230), 2)

cv2.imshow('Orig', img)
cv2.imshow('Image gray', img_gray)
cv2.imshow('Threshold', thresh)
cv2.imshow('Canny', canny)


"""
Причина, по которой мы получаем разное количество контуров, заключается в том, 
что мы применяем детектор края кенни к нашему полутоновому изображению. 
Это дает результат «белых линий» - краев на пустом изображении.
Получаются "отдельные" линии, которые также явлюятся контурами.
"""







circle = cv2.imread('circle.png')
circle_gray = cv2.cvtColor(circle, cv2.COLOR_BGR2GRAY)
_, thresh_circle = cv2.threshold(circle_gray, 150, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh_circle, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print('Количество контуров: '+ str(len(contours)) + '\n')
cv2.drawContours(circle, contours, 1, (28, 255, 249), 2)
cv2.drawContours(circle, contours, 2, (255, 0, 0), 2)

outside = contours[1]
inside = contours[2]

'''
cv2.contourArea()
The function computes a contour area. Similarly to moments , the area is computed using the Green formula. 
Thus, the returned area and the number of non-zero pixels. 
Also, the function will most certainly give a wrong results for contours with self-intersections.
'''

print('Периметр контура внешней окружности: ' + str(cv2.arcLength(outside, True)))
print('Площадь контура внешней окружности: ' + str(cv2.contourArea(outside)))
# Получим координаты внешнего ограничивающего прямоугольника:
x, y, w, h = cv2.boundingRect(outside)
# Нарисуем внешний огр.прямоугольник:
cv2.rectangle(circle, (x, y), (x + w, y + h), (0, 255, 0), 2)
print('Площадь внешнего ограничивающего прямоугольника: '+ str(w*h))
# Получим координаты внешней описанной окружности:
(x,y),radius = cv2.minEnclosingCircle(outside)
center = (int(x),int(y))
radius = int(radius)
# Нарисуем внешнюю ограничивающую окружность:
cv2.circle(circle,center,radius,(0, 0, 255), thickness = 2)
print('Площадь внешней ограничивающей окружности: ' + str(pi*(radius**2)) + '\n')


print('Периметр контура внутренней окружности: ' + str(cv2.arcLength(inside, True)))
print('Площадь контура внутренней окружности: ' + str(cv2.contourArea(inside)))
# Получим координаты внутреннего ограничивающего прямоугольника:
x, y, w, h = cv2.boundingRect(inside)
# Нарисуем внутренний огр.прямоугольник:
cv2.rectangle(circle, (x, y), (x + w, y + h), (133, 21, 199),2)
print('Площадь внутреннего ограничивающего прямоугольника: '+ str(w*h))
# Получим координаты внутренней ограничивающей окружности:
(x,y),radius = cv2.minEnclosingCircle(inside)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(circle,center,radius,(0,69,255),2)
print('Площадь внутренней ограничивающей окружности: ' + str(pi*(radius**2)) + '\n')

cv2.imshow('Circle', circle)

cv2.waitKey(0)
cv2.destroyAllWindows()