from cv2 import cv2

"""Дополнительное задание"""

# Изображение 1
lr41 = cv2.imread('LR_4_1.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)
print(type(lr41))
print(lr41)
max_ind = lr41.max().max()
min_ind = lr41.min().min()
for i in range(len(lr41)):
    for j in range(len(lr41[1])):
        lr41[i,j] = lr41[i,j] - min_ind
        lr41[i,j] = lr41[i,j] / (max_ind - min_ind) * 255

# Изображение 2
lr42 = cv2.imread('LR_4_2.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)
max_ind = lr42.max().max()
min_ind = lr42.min().min()
for i in range(len(lr42)):
    for j in range(len(lr42[1])):
        lr42[i,j] = lr42[i,j] - min_ind
        lr42[i,j] = lr42[i,j] / (max_ind - min_ind) * 255

# Изображение 3
lr43 = cv2.imread('LR_4_3.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)
max_ind = lr43.max().max()
min_ind = lr43.min().min()
for i in range(len(lr43)):
    for j in range(len(lr43[1])):
        lr43[i,j] = lr43[i,j] - min_ind
        lr43[i,j] = lr43[i,j] / (max_ind - min_ind) * 255

cv2.imshow('LR_4_1_FIX.png', lr41)
cv2.imshow('LR_4_2_FIX.png', lr42)
cv2.imshow('LR_4_3_FIX.png', lr43)


cv2.waitKey(0)
cv2.destroyAllWindows()