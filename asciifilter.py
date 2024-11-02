import cv2
import numpy as np
import tkinter as tk
import threading

# More detailed ASCII characters for better representation
ASCII_CHARS = '@%#*+=-:. '  # You can expand this with more characters if desired

def resize_image(image, new_width=160):
    (original_height, original_width) = image.shape[:2]
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * new_width * 0.55)
    return cv2.resize(image, (new_width, new_height))

def grayify(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def pixels_to_ascii(image):
    pixels = image.flatten()
    ascii_str = ''.join(ASCII_CHARS[min(pixel // (256 // len(ASCII_CHARS) - 1), len(ASCII_CHARS) - 1)] for pixel in pixels)
    return ascii_str


def update_frame():
    global cap
    while True:
        ret, frame = cap.read()
        if ret:
            frame = resize_image(frame)
            gray_frame = grayify(frame)
            ascii_str = pixels_to_ascii(gray_frame)

            img_width = frame.shape[1]
            ascii_str_len = len(ascii_str)
            ascii_img = "\n".join(ascii_str[i:i + img_width] for i in range(0, ascii_str_len, img_width))

            # Update the label with the ASCII art
            ascii_label.config(text=ascii_img)

def start_video():
    threading.Thread(target=update_frame, daemon=True).start()

# Initialize the main window
root = tk.Tk()
root.title("ASCII Art Live Feed")

# Set the desired window size
root.geometry("800x600")  # Width x Height

# Create a label to display ASCII art
ascii_label = tk.Label(root, font=("Courier", 6), bg="black", fg="white", padx=5, pady=5)
ascii_label.pack(expand=True, fill=tk.BOTH)

# Open a connection to the webcam
cap = cv2.VideoCapture('http://10.0.0.14:4747/video') # Add custom ip here

# Start the video thread
start_video()

# Run the Tkinter main loop
root.mainloop()

# Release the webcam
cap.release()
