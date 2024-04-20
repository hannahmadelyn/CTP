#Riley Parsons

#Refernces
# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# https://cloudinary.com/glossary/edge-detection
# https://www.youtube.com/watch?v=KwbDA_0RU9o
# https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de
# https://www.geeksforgeeks.org/python-opencv-canny-function/


import numpy as np
import cv2 as cv

videoInput = cv.VideoCapture('Mantis_Shrimp_Destroys_Clam.mp4')

# Thresholds
tLower = 60
tUpper = 120

replay = True

print("Press the q key on the keyboard to exit the program.")

while replay:
    videoInput.set(cv.CAP_PROP_POS_FRAMES, 0)
    
    while videoInput.isOpened():
        ret, video = videoInput.read()
    
        #if frame is read correctly ret is ture
        if not ret:
            print("Replaying Video")
            break

        # stadard video output
        garry = cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    
        #Canny(video_Input/image, threshold1, threshold2 )
        #Thresholds are for hysteresis \procedure
        #Threshold 1: minVal, Threshold 2: maxVal
        #Any Values which lie between these 2 thesholds are callifed edges or non edges based on the connectivity
        # if they are connected to sure edge pixles they are considerd to be part of edges
        edge = cv.Canny(garry, tLower, tUpper)
    
        #Apeture Size
        #this is used to calculate the gradiet in the canny edge detection. 
        #default value = 3. should be between 3 and 7 and an odd number.
        # increasing the size will increase the detail
        apetureEdgeUp = cv.Canny(garry, tLower, tUpper, apertureSize= 5)
    

        #L2Gradient
        #  a boolean parameter that specifies if you want to calculate the usual gradient eqation or l2G algorithm
        # another optional include
        #L2 = Square root (Gradient_xSqaure + Gradient_y_square)
        #L1 = absolute value (gradient_x) + absolute value (gradient_y)
        l2 = cv.Canny(garry, tLower, tUpper, L2gradient = True)
    
        # Combining L2 and Apeture 
        combo = cv.Canny(garry, tLower, tUpper, apertureSize= 5, L2gradient= True)

        # This is testing the filtering options outlined above to make both the mantis shrimp and clam more clear and reducing the noise in the background
        # Future testing will aim to reduce the noise before applying edge detection
        clarityTest = cv.Canny(garry, 150, 200, L2gradient= True)


        #Display resulting frame/ image to window with colour properties garry https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
        # imshow(const string, windname)
        cv.imshow('Original', garry)
        cv.imshow('Edge Detection', edge)
        cv.imshow('Increased Apeture Size', apetureEdgeUp)
        cv.imshow('L2 Gradient Version', l2)
        cv.imshow('L2 Gradient and Increased Apeture Size', combo)
        cv.imshow('Clarity Testing', clarityTest)
        
        #1 ms from keypress. break out of inner loop
        if cv.waitKey(1) == ord('q'):
            replay = False
            break
        
#once the program has completed release the capture and close
print("Program ending")        
videoInput.release()
cv.destroyAllWindows()
