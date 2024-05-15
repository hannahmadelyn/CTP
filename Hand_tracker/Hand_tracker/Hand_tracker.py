#Riley Parsons
from mimetypes import init
import numpy as np
import sys
import cv2 as cv
print("OpenCV version: ", cv.__version__)

# references
# https://www.futurelearn.com/info/courses/introduction-to-image-analysis-for-plant-phenotyping/0/steps/305359
# https://learnopencv.com/object-tracking-using-opencv-cpp-python/
# https://docs.opencv.org/3.4/d2/dff/classcv_1_1TrackerKCF.html
# https://www.youtube.com/watch?v=OUAZrY9iRgE

# purely testing with mantis shrimp. Once a good video involving hand movments is available will change
videoInput = cv.VideoCapture("Mantis_Shrimp_Destroys_Clam.mp4")
# video filters

# https://docs.opencv.org/3.4/d0/d0a/classcv_1_1Tracker.html
#KCF tracking seems to be the best starting choice
# https://docs.opencv.org/3.4/d2/dff/classcv_1_1TrackerKCF.html#details
#GOTURN: generic object tracking using regression networks
# Deep learning object based algorithm. does not work in this program currently for anything
# I think thik GOTURN will be overkill for this project
#https://learnopencv.com/goturn-deep-learning-based-object-tracking/

#creating tracker object
#Note: you will need to install additional modules that are not part of the main
# pip install opencv-contrib-python

# note: different implamentations

trackerType =['KCF', 'MOSSE', 'TLD', 'MIL', 'CSRT']

trackerSelect = trackerType[4]
if trackerSelect == 'KCF':
    tracker = cv.TrackerKCF.create()
    edgeTracker = cv.TrackerKCF.create()
if trackerSelect == 'MOSSE':
    tracker = cv.legacy.TrackerMOSSE.create()
    edgeTracker = cv.legacy.TrackerMOSSE.create()
if trackerSelect == 'TLD':
    tracker = cv.legacy.TrackerTLD.create()
    edgeTracker = cv.legacy.TrackerTLD.create()
if trackerSelect == 'MIL':
    tracker = cv.TrackerMIL.create()
    edgeTracker = cv.TrackerMIL.create()
if trackerSelect == 'CSRT':
    tracker = cv.TrackerCSRT.create()
    edgeTracker = cv.TrackerCSRT.create()

#tracker = cv.TrackerGOTURN.create()

# Identify Frames in video input. This will be useful for frame extraction
fps = videoInput.get(cv.CAP_PROP_FPS)
print('Frames per second: ',fps)
# mantis shrimp video is 30 fps

# CAP_PROP_POS_FRAMES is a reference frame position
# selectiing first frame in video 0
# videoInput.set(cv.CAP_PROP_POS_FRAMES, 0)

if not videoInput.isOpened():
    print("Unable to open video.")
    sys.exit()
    
#selecting initial object to track
success, frame = videoInput.read()
cv.imshow(trackerSelect, frame)
# to confirm input press space or enter
videoInput.set(cv.CAP_PROP_POS_FRAMES, 0)

# addition variations footage for tracker demonstrations

#test if Frame is an empty value
if frame is None:
    print("Frame is empty.")
    sys.exit()

#bounding box for tracking once video ahs been exited via c button
# select roi allow you to create the bounding box information    
bbox = cv.selectROI(frame, False)
print("Bounding Box selection: ", bbox)
print("Frame Details, is frame selection true?: ", frame)

#this is the default position and if the bounding box is ever created with this profile it will be a user error as it is the 0 pixle more or less
if bbox == (0,0,0,0):
    print("invalid location. bounding box error.")
    sys.exit()

#initilize tracker
tracking = tracker.init(frame,bbox)
edgeTracking = tracker.init(frame,bbox)
# program creaetes a new window for the selector which we do not need anymore
cv.destroyWindow("ROI selector")

#success is a bool
while videoInput.isOpened():
    #continue reading the video
    success, frame = videoInput.read()
    
    if not success:
        print("unable to read video file.")
        break
    
    #edge detection settings
    edge = cv.Canny(frame,160,240)

    # in the loop of playing the video update the tracker
    success, bbox = tracker.update(frame)
    if success:
        #top left of bounding box
        pointer1 = (int(bbox[0]), int(bbox[1]))
        #bottom right cornder of nbox
        pointer2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        # creating rectngle. onto the frame here. variables pointer 1 and pointer 2. we have rgb colour and line thickness. it will appear on the tracking window
        cv.rectangle(frame, pointer1, pointer2, (0,255,0), 2, 2)
    
        #tracking for edge detection bounding box
    success, edgeBbox = tracker.update(edge)
    if success:
        pointer1 = (int(edgeBbox[0]), int(edgeBbox[1]))
        pointer2 = (int(edgeBbox[0] + edgeBbox[2]), int(edgeBbox[1] + edgeBbox[3]))
        cv.rectangle(edge, pointer1, pointer2, (0,255,0), 2, 2)
        

    cv.imshow(trackerSelect, frame)
    cv.imshow("Edge Detection", edge)

    if cv.waitKey(1) == ord("q"):
        break
# the aim here is to display the first frame so the user can select an object to track
videoInput.release()
cv.destroyAllWindows()