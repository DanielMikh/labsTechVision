from cv2 import cv2
from matplotlib import pyplot as plt

""" 
Задание 1: 
Изображения с четкими границами: автомобиль('vaz.png'), пЫНЯ('Putin.png'), логотип OpenCV('open-logo.png');
Изображения с нечеткими границами: лес('forest.png') и хамелеон('chameleon.png')
"""

# img = cv2.imread('vaz.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)
# img = cv2.imread('Putin.png', cv2.IMREAD_REDUCED_GRAYSCALE_4)
# img = cv2.imread('forest.png', cv2.IMREAD_REDUCED_COLOR_4)
# img = cv2.imread('chameleon.png', cv2.IMREAD_REDUCED_COLOR_2)
img = cv2.imread('open-logo.png', cv2.IMREAD_GRAYSCALE)


"""
Чем порядок производной больше, тем границы на изображении более размыты, появляется шум на изображении; 
Порядок производной должен быть СТРОГО меньше размера ядра Собеля(ksize). По умолчанию ksize = 3;
Оператор Собеля 'ksize' вычисляет градиент яркости изображения в каждой точке, 
участки с большой величиной градиента (в основном, грани) будут видны как белые линии;
Параметр ddepth - глубина выходного изображения. Возьмем 'cv2.CV_8U', что означает создание 8bit unsigned numpy array
"""
sobel_x = cv2.Sobel(src = img, ddepth = cv2.CV_8U, dx = 1, dy = 0, ksize = 3)
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1)
sobel_xy = cv2.Sobel(img, cv2.CV_8U, 1, 1)

'''Оператор Лапласа идеально подходит для изображений с четкими границами'''
laplacian = cv2.Laplacian(img,cv2.CV_8U, cv2.BORDER_DEFAULT)

'''
Перед использованием детектора границ Кенни рекомендуется выполнить размытие;
Отклонение от ядра по осям X,Y -> (x,y), где x,y целые нечетные числа
'''
blur = cv2.GaussianBlur(img,(1,1), cv2.BORDER_DEFAULT)

'''
threshold1 - порог минимума, threshold2 - порог максимума;
apertureSize - размер для оператора Собеля. apertureSize = 3 по дефолту;
L2gradient если True, то вычисляется точно, если False, то вычисляется упрощенно
'''
canny = cv2.Canny(image = blur, threshold1 = 200, threshold2 = 225, apertureSize = 3, L2gradient = True)

"""
!!!Matplotlib.pyplot.imshow() принимает параметр "cmap", который ИГНОРИРУЕТСЯ ТОЛЬКО для RGB изображений!!!
6 изображений на 1-ой фигуре выглядят так, что невозможно найти разницу между ними.
Пример вывода я оставлю, а в дальнейшем буду пользоваться выводом на экран с помощью библиотеки openCV

plt.subplot(3, 2, 1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 2), plt.imshow(sobel_x, cmap = 'gray')
plt.title('Sobel_x'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 3), plt.imshow(sobel_y, cmap = 'gray')
plt.title('Sobel_y'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4), plt.imshow(sobel_xy, cmap = 'gray')
plt.title('Sobel_xy'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 5), plt.imshow(laplacian, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 6), plt.imshow(canny, cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()
"""

cv2.imshow('Original', img)
cv2.imshow('Sobel_x', sobel_x)
cv2.imshow('Sobel_y', sobel_y)
cv2.imshow('Sobel_xy', sobel_xy)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()