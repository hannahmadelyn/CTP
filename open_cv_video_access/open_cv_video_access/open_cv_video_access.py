# Riley Parsons
# following this tutorial
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('Bang_Bang_Bang_Gigguk.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    
    #if frame is read correctly ret is ture
    if not ret:
        print("cannot recieve frame (stream end?). exiting")
        break
    
    garry = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Display resulting frame/ image to window with colour properties garry https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
    # imshow(const string, windname)
    cv.imshow('Video', garry)
    if cv.waitKey(1) == ord('q'):
       break

#once the program has completed release the capture and close
cap.release()
cv.destroyAllWindows()