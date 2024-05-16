#change control
# Riley Parsons: created class and defined all methods with pass and constructor. filled in basic implamentation for methods except detect 16/05/2024


import cv2 as cv

#constructor
# if we need multiple trackers we may want ot create a tracker ID
class tracker(object):
    def __init__(self, bBox, frame):
        self.bBox = bBox
        self.frame = frame
        #init tracker 
        self.tracker = cv.TrackerCSRT.create()
    

    #methods
    def initTracker(self):
        bbox
        self.tracker.init(self.frame, bbox)
    
    # update tracker with the new frames
    def update(self):
        success, bbox = self.tracker.update(self.frame)
        if success:
            self.bBox = bbox
    
    # return current bounding box. x,y,width,height
    def passBbox(self):
        return self.bBox
    

    # this method is to be implamented once basic functionality of program is completed
    def detect(self):
        pass