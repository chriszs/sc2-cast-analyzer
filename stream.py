import pafy
import cv2

url = 'https://youtu.be/zoIeC19F3q8'
video = pafy.new(url)

print(video.title)

play = video.getbest(preftype='mp4')

#start the video
cap = cv2.VideoCapture(play.url)
while (True):
    ret,frame = cap.read()
    """
    your code....
    """
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

cap.release()
cv2.destroyAllWindows()
