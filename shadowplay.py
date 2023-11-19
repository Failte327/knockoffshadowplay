import pyautogui
import cv2
import numpy as np
import time
from tkinter import *
from tkinter import ttk

global recording
recording = True

def start_recording():
    recording = True
    print(f"recording = {recording}")

def stop_recording():
    recording = False
    print(f"recording = {recording}")

timestamp = time.time()
screen_size = (1920, 1080)
fps = 60
output_filename = f"{timestamp}.avi"

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, fourcc, fps, screen_size)
print("Starting program")

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="DAoC Recorder").grid(column=0, row=0)
ttk.Button(frm, text="Start Recording", command=start_recording()).grid(column=1, row=0)
ttk.Button(frm, text="Stop Recording", command=stop_recording()).grid(column=1, row=1)

root.mainloop()

while recording == True:
    # Capture screen content
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    # Convert BGR format (used by OpenCV) to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    if (recording == False):
        break

# Release the VideoWriter and close the OpenCV windows
out.release()
cv2.destroyAllWindows()