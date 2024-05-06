import cv2

#The path to the video file for extraction 
video_path = 'C:\\Users\\Avi\\Downloads\\Bang_Bang_Bang_Gigguk.mp4'


# Using OpenCV to capture the video 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
interval = int(fps / 2)
frame_num = 0

Key_frames_count = 0

while True:
    # Reading the frame 
    success, frame = cap.read()

    if not success:
        break

    # If the frame is read correctly, save it as an image
    if frame_num % interval == 0:
        cv2.imwrite(f'frame_{frame_num}.jpg', frame)
        frame_num += 1
    if Key_frames_count >= 10:
        break 

    frame_num += 1

# Release the video capture object, also close windows
cap.release()
cv2.destroyAllWindows()


