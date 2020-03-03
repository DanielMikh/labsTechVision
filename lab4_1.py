from cv2 import cv2 

# реализация своей функции "cv2.treshold()"

picture = 'Putin.png'
maxValue = 255

def treshold(image, Value):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    cv2.imshow('Putin before', img)

    for i in range(len(img)):
        for j in range(len(img[1])):
            if img[i, j] > 128:
                img[i, j] = Value
            else:
                img[i, j] = 0

    cv2.imshow('Putin after', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

treshold(picture, maxValue)