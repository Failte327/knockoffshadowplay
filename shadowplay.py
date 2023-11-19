import pyautogui
import cv2
import numpy as np
import time

timestamp = time.time()
screen_size = (1920, 1080)
fps = 60
output_filename = f"{timestamp}.avi"

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, fourcc, fps, screen_size)
print("Starting recording")

while True:
    # Capture screen content
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    # Convert BGR format (used by OpenCV) to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    # Stop recording when the user presses the 'q' key (not currently working)
    if cv2.waitKey(1) == ord("q"):
        print("Stopping recording")
        break

# Release the VideoWriter and close the OpenCV windows
out.release()
cv2.destroyAllWindows()