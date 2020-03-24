from cv2 import cv2

img = cv2.imread('5_2.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

'''
epsilon отвечает за точность аппроксимации;
так как мы итерируем, то каждый обход(шаг) у нас будет только 1 контур -> contourIdx = 0;
contours = [approx] в [], т.к drawContours ожидает массив (список в случае Python) контуров, 
а не только один массив (который возвращается из approxPolyDP).
'''
for contour in contours:
    approx = cv2.approxPolyDP(curve = contour, epsilon = 0.01 * cv2.arcLength(contour, True), closed = True)
    if len(approx) == 3:
        cv2.drawContours(image = img, contours = [approx], contourIdx = 0, color = (0, 0, 255), thickness = 3)
    elif len(approx) == 4:
        cv2.drawContours(img, [approx], 0, (255, 0, 0 ), 3)
    else:
        cv2.drawContours(img, [approx], 0, (0, 255, ), 3)


cv2.imshow('Shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows