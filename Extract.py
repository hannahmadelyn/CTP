import cv2

#The path to the video file for extraction 
video_path = 'C:\\Users\\Avi\\Downloads\\Bang_Bang_Bang_Gigguk.mp4'


# Using OpenCV to capture the video 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_num = 0
while True:
    # Read a frame
    success, frame = cap.read()

    # If the frame is read correctly, save it as an image
    if success:
        cv2.imwrite(f'frame_{frame_num}.jpg', frame)
        frame_num += 1
    else:
        break

# Release the video capture object, also close windows
cap.release()
cv2.destroyAllWindows()