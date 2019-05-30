from imutils.object_detection import non_max_suppression
import pytesseract
import pafy
import cv2
import re

# url = 'https://youtu.be/zoIeC19F3q8'
# video = pafy.new(url)

# print(video.title)

# play = video.getbest(preftype='mp4')

TESS_CONFIG = ('-l eng --oem 1 --psm 12')

def read_box(frame,w,h,y,x,ocr,name):
    box = frame[y:y+h, x:x+w].copy()
    box = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
    box = cv2.bitwise_not(box)
    # ret,box = cv2.threshold(box,100,255,cv2.THRESH_BINARY_INV)

    # cv2.imshow(name,box)

    text = None

    if ocr:
        text = pytesseract.image_to_string(box, config=TESS_CONFIG)
        print(re.sub(r"\s+", ' ', text))

    return box, text

i = 0

#start the video
cap = cv2.VideoCapture('data/sample.mp4') # play.url)
while (True):
    ret,frame = cap.read()

    if frame is None:
        break

    (origH, origW) = frame.shape[:2]

    w = 600-140
    x = 360

    box1,text1 = read_box(frame,w,28,origH-72,x,i % 60 == 0,'box1')
    # box1,text1 = read_box(frame,w,28,origH-72,x,i % 60 == 0,'box1')

    # box2,text2 = read_box(frame,w,12,origH-43,x,i % 60 == 0,'box2')

    box3,text3 = read_box(frame,w,28,origH-30,x,i % 60 == 0,'box3')
    # box3,text3 = read_box(frame,w,28,origH-30,x,i % 60 == 0,'box3')

    i += 1

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

cap.release()
cv2.destroyAllWindows()
