from cv2 import cv2
''' 
    Применить на практике бинаризацию всех типов для изображений.
    Подобрано по 2 примера изображений на каждый тип, иллюстрирующие разницу результатов использованных методов.
'''

"""Для дорог лучше подходит метод TRESH_TOZERO, т.к. картинка монотонна, а полученное изображение четчё при ручном подборе трешхолда"""
img = cv2.imread('Doroga1.png', cv2.IMREAD_GRAYSCALE)

treshold, img1 = cv2.threshold(img, thresh = 200, maxval = 255, type = cv2.THRESH_TOZERO)
treshold, img2 = cv2.threshold(img, 200, 255, cv2.THRESH_OTSU)
img3 = cv2.adaptiveThreshold(img, maxValue = 255, adaptiveMethod = cv2.ADAPTIVE_THRESH_MEAN_C, 
thresholdType = cv2.THRESH_BINARY, blockSize = 11, C = -4)


img_2 = cv2.imread('Doroga2.png', cv2.IMREAD_GRAYSCALE)

treshold, img4 = cv2.threshold(img_2, 200, 255, cv2.THRESH_TOZERO)
treshold, img5 = cv2.threshold(img_2, 200, 255, cv2.THRESH_OTSU)
img6 = cv2.adaptiveThreshold(img_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -4)

"""Для сканов лучше подходит как адаптивный метод, так и TRESH_OTSU, т.к. скан документа не монотонный"""
# img = cv2.imread('Scan1.png', cv2.IMREAD_GRAYSCALE)

# treshold, img1 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
# treshold, img2 = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
# img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 30)


# img_2 = cv2.imread('Scan2.png', cv2.IMREAD_GRAYSCALE)

# treshold, img4 = cv2.threshold(img_2, 128, 255, cv2.THRESH_TOZERO)
# treshold, img5 = cv2.threshold(img_2, 128, 255, cv2.THRESH_OTSU)
# img6 = cv2.adaptiveThreshold(img_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 29, 30)

"""Для фото написанного от руки также подходит лучше адаптивный, так как происходят резкие изменения уровня яркости на небольших расстояних"""
# img = cv2.imread('Text1.png', cv2.IMREAD_GRAYSCALE)

# treshold, img1 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
# treshold, img2 = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
# img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 15)


# img_2 = cv2.imread('Text2.png', cv2.IMREAD_GRAYSCALE)

# treshold, img4 = cv2.threshold(img_2, 128, 255, cv2.THRESH_TOZERO)
# treshold, img5 = cv2.threshold(img_2, 128, 255, cv2.THRESH_OTSU)
# img6 = cv2.adaptiveThreshold(img_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 29, 15)

cv2.imshow('Tresh_tozero', img1)
cv2.imshow('Tresh_otsu', img2)
cv2.imshow('Tresh_adaptive', img3)
cv2.imshow('Tresh_tozero2', img4)
cv2.imshow('Tresh_otsu2', img5)
cv2.imshow('Tresh_adaptive2', img6)



cv2.waitKey(0)
cv2.destroyAllWindows()