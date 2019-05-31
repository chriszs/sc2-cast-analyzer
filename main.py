import cv2
import sys
import numpy as np

# based on
# https://cvisiondemy.com/extract-roi-from-image-with-python-and-opencv/
# and https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/

def read_box(frame,width,height,boxX,boxY,name):
    box = frame[boxY:boxY+height, boxX:boxX+width].copy()
    gray = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY).copy()
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    ret, ocrable = cv2.threshold(gray, 80, 255, cv2.THRESH_TOZERO)
    ocrable = cv2.bitwise_not(ocrable).copy()
    # ret, ocrable = cv2.threshold(ocrable, 200, 255, cv2.THRESH_TOZERO)

    kernel = np.ones((10,6), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)

    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    text = []

    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)

        padding = 1
        if x-padding > 0:
            x -= padding
        if x+w+padding*2 < width:
            w += padding*2

        roi = ocrable[y:y + h, x:x + w]

        if h <= height * 0.3:
            continue

        # cv2.rectangle(ocrable, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # cv2.imshow(name, ocrable)
    # cv2.waitKey(0)

    return box

frame = cv2.imread(sys.argv[1])

(origH, origW) = frame.shape[:2]

w = 600
x = 190
h = 72

name = 'stats'

box1 = read_box(frame, w, h, x, origH-h, name)

print(sys.argv[2] + name + '.png')
# cv2.imwrite(box1, sys.argv[2] + name + '.png')

cv2.destroyAllWindows()
