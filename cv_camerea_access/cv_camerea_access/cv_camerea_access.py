# Riley Parsons 
# following this tutorial
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

#import Numpy
import numpy as np
#import OpenCV
import cv2 as cv

#for opening the camera. videoCapture(0) will relate to boolean in this case 0 is true
capture = cv.VideoCapture(0)
#in case of errors in accessing camera
if not capture.isOpened():
    print("Cannot Open Camera")
    exit()
    
#camera recording loop
while True:
    # frame by frame video capture
    ret, frame = capture.read()
    
    if not ret:
        print("can not recieve frame (stream end?). Exiting...")
        break

    #operations on the frame are here
    garry = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 
    
    #Display resulting frame/ image to window with colour properties garry https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
    # imshow(const string, windname)
    cv.imshow('WebCam', garry)
    #press q to quit
    if cv.waitKey(1) == ord('q'):
        break
    
#once everything has been completed release the capture
capture.release()
cv.destroyAllWindows()
