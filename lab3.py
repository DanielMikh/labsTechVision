from cv2 import cv2
import numpy as np
import pprint
print('OpenCD verison:', cv2.__version__)

# Загрузить изображение 
img = cv2.imread('default.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Сохранить изображение как 'имя.png' 
cv2.imwrite('gray.png', gray_img)

gray_img2 = np.copy(gray_img)

# Проходим по каждому элементу массива и инвертируем его в диапазоне 0...255
# Закомментировано, так как ниже приведен способ проще, быстрее
# for i in range(len(gray_img2)):
#     for j in range(len(gray_img2[i])):
#         gray_img2[i][j] = 255 - gray_img2[i][j]

gray_img2 = 255 - gray_img2

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(rgb_img.shape)

# Можно обойтись и без создания массива из нулей такого же размера, так как merge сделает своё дело
# new = np.zeros(rgb_img.shape)

red = rgb_img[:,:,0]
print("RED: ", red)
green = rgb_img[:,:,1]
print("GREEN: ", green)
blue = rgb_img[:,:,2]
print("BLUE :", blue)

# # merge - слияние, здесь цвета в порядке BGR
new = cv2.merge((red, green, blue))


# cv2.imshow() - метод, который показывает изображение в отдельном окне
# Дефолтное изображение; серое; инверсия серого
cv2.imshow('Default', img)
cv2.imshow('Gray', gray_img)
cv2.imshow('InversionGray', gray_img2)

# Изображение, где поменяны местами каналы
cv2.imshow('BGR -> RGB', new)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Сохранит два изображения после закрытия:
cv2.imwrite('inversion.png', gray_img2)
cv2.imwrite('BGRtoRGB.png', new)


