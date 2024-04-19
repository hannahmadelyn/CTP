#Riley Parsons

# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# https://cloudinary.com/glossary/edge-detection
# https://www.youtube.com/watch?v=KwbDA_0RU9o
# https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de

import numpy as np
import cv2 as cv

#videoInput = cv.VideoCapture('All_Joey.mp4')
videoInput = cv.VideoCapture('Japanese_Goblin.mp4')

#while true
while videoInput.isOpened():
    ret, video = videoInput.read()
    
    #if frame is read correctly ret is ture
    if not ret:
        print("cannot recieve video (end?). exiting")
        break
    
     #program crashes at the end currently
    garry = cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    #Canny(video_Input/image, threshold1, threshold2 )
    #Thresholds are for hysteresis \procedure
    #Threshold 1: minVal, Threshold 2: maxVal
    #Any Values which lie between these 2 thesholds are callifed edges or non edges based on the connectivity
    # if they are connected to sure edge pixles they are considerd to be part of edges
    edge = cv.Canny(garry, 60, 120)
    
    #Display resulting frame/ image to window with colour properties garry https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
    # imshow(const string, windname)
    cv.imshow('Video', edge)   #change edge to garry to see normal video
    if cv.waitKey(1) == ord('q'):
       break

#once the program has completed release the capture and close
videoInput.release()
cv.destroyAllWindows()