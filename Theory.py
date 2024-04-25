'''

1.What is a Frame in Video?
   - Think of a video as a book. Each page of the book is a still image, and these pages are called "frames."
     When you flip through them quickly, it appears as moving images. So, in video terms, a frame is just one of those still images. 

2.Understanding the Script:
   - OpenCV Library: This script uses a library called OpenCV to handle video processing. It is a commonly used for tasks involving images and videos, like reading videos, capturing frames, others.

   - Capture Video: The script starts by opening the video file `Bang_Bang_Bang_Gigguk.mp4` from a specified path. If it fails to open, it prints an error message.

   - FPS and Interval Calculation:
     - FPS (Frames Per Second): This is how many frames appear on the screen every second. For example, at 30 fps, 30 frames are shown each second.
     - Interval Calculation: The script calculates an interval to capture frames every half-second. If the video is 30 fps, half a second is 15 frames. The script will look at every 15th frame.

   - Loop Through Frames:
     - The script reads each frame one by one in a loop. If it reads a frame successfully, it proceeds; if not it stops the loop.

   - Save Key Frames:
     - The script saves a frame only if the current frame number modulo (`%`) the interval (half-second) is zero. This means it only saves every 15th frame,
       for example, capturing the frame at each half-second mark.
     - It keeps a count of how many frames have been saved (`key_frame_count`). Once it saves 10 frames, it stops to avoid saving too many.

   - End of Script:
     - After exiting the loop (either by reading all frames or after saving 10 key frames), the script releases the video file and cleans up, ensuring that all resources are properly closed.






















'''