import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np
base_img = cv2.imread("base.png")

capture = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('video_capture.avi', fourcc, 6, (640,480))
 
while (True):
 
    ret, frame = capture.read()
     
    if ret:
        #cv2.imshow('video', frame)
        s = ssim(base_img,frame,multichannel=True)
        if(s <0.7):
            videoWriter.write(frame)
        print(s)

 
    if cv2.waitKey(1) == 27:
        break
 
capture.release()
videoWriter.release()
 
cv2.destroyAllWindows()