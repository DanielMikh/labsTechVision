from cv2 import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

color_yellow = (0,255,255)
color_blue = (255,0,0)

cv2.rectangle(img,(0,512),(512,256),color_yellow,-1)
cv2.rectangle(img,(0,0),(512,256),color_blue,-1)

# np.zeroes(y, x, кол-во каналов)
img2 = np.zeros((210,512,3), dtype = np.uint8)
# в openCV цвета в порядке BGR - blue, green, red
# Синий
cv2.line(img2,(0,10),(512,10),(255,0,0),20)
# Зеленый
cv2.line(img2,(0,40),(512,40),(0,255,0),20)
# Красный
cv2.line(img2,(0,70),(512,70),(0,0,255),20)
# Фиолетовый
cv2.line(img2,(0,100),(512,100),(125,0,125),20)
# Коричневый
cv2.line(img2,(0,130),(512,130),(0,60,125),20)
# Серый
cv2.line(img2,(0,160),(512,160),(100,100,100),20)
# Абрикосовый
cv2.line(img2,(0,190),(512,190),(100,150,250),20)


cv2.imshow('Ukraine', img)
cv2.imshow('Different colors', img2)

cv2.waitKey(0)
cv2.destroyAllWindows() 