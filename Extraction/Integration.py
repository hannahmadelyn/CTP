from mimetypes import init
import numpy as np
import sys
import cv2 as cv
print("OpenCV version: ", cv.__version__)

videoInput = cv.VideoCapture("C:\\Users\\Avi\\Mantis_Shrimp_Destroys_Clam.mp4")

trackerType = ['KCF', 'MOSSE', 'TLD', 'MIL', 'CSRT']
trackerSelect = trackerType[4]
if trackerSelect == 'KCF':
    tracker = cv.TrackerKCF.create()
    edgeTracker = cv.TrackerKCF.create()
elif trackerSelect == 'MOSSE':
    tracker = cv.legacy.TrackerMOSSE.create()
    edgeTracker = cv.legacy.TrackerMOSSE.create()
elif trackerSelect == 'TLD':
    tracker = cv.legacy.TrackerTLD.create()
    edgeTracker = cv.legacy.TrackerTLD.create()
elif trackerSelect == 'MIL':
    tracker = cv.TrackerMIL.create()
    edgeTracker = cv.TrackerMIL.create()
elif trackerSelect == 'CSRT':
    tracker = cv.TrackerCSRT.create()
    edgeTracker = cv.TrackerCSRT.create()

fps = videoInput.get(cv.CAP_PROP_FPS)
print('Frames per second: ', fps)

if not videoInput.isOpened():
    print("Unable to open video.")
    sys.exit()

success, frame = videoInput.read()
cv.imshow(trackerSelect, frame)

videoInput.set(cv.CAP_PROP_POS_FRAMES, 0)

if frame is None:
    print("Frame is empty.")
    sys.exit()

bbox = cv.selectROI(frame, False)
print("Bounding Box selection: ", bbox)
print("Frame Details, is frame selection true?: ", frame)

if bbox == (0, 0, 0, 0):
    print("invalid location. bounding box error.")
    sys.exit()

tracking = tracker.init(frame, bbox)
edgeTracking = tracker.init(frame, bbox)

cv.destroyWindow("ROI selector")

# Frame extraction settings
interval = int(fps / 2)  # Capture a frame every half second
frame_num = 0
key_frames_count = 0

while videoInput.isOpened():
    success, frame = videoInput.read()

    if not success:
        print("Unable to read video file.")
        break

    # Save frames every half second
    if frame_num % interval == 0 and key_frames_count < 10:
        frame_path = f'key_frame_{key_frames_count}.jpg'
        cv.imwrite(frame_path, frame)
        key_frames_count += 1

    # Tracking logic
    success, bbox = tracker.update(frame)
    if success:
        pointer1 = (int(bbox[0]), int(bbox[1]))
        pointer2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv.rectangle(frame, pointer1, pointer2, (0, 255, 0), 2, 2)

    edge = cv.Canny(frame, 160, 240)
    success, edgeBbox = tracker.update(edge)
    if success:
        pointer1 = (int(edgeBbox[0]), int(edgeBbox[1]))
        pointer2 = (int(edgeBbox[0] + edgeBbox[2]), int(edgeBbox[1] + edgeBbox[3]))
        cv.rectangle(edge, pointer1, pointer2, (0, 255, 0), 2, 2)

    cv.imshow(trackerSelect, frame)
    cv.imshow("Edge Detection", edge)

    if cv.waitKey(1) == ord('q'):
        break

    frame_num += 1

videoInput.release()
cv.destroyAllWindows()
