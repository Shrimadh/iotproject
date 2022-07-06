import cv2
import numpy as np
capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while (True):
 
    ret, frame = capture.read()
     
    if ret:
        cv2.imshow('video', frame)
    
    if cv2.waitKey(1) == 97:
        cv2.imwrite("base.png",frame)
        
    if cv2.waitKey(1) == 27:
        break
 
capture.release() 
cv2.destroyAllWindows()