
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Select image from computer
root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Error: Please select a valid image!")
else:
    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Perform dilation
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    # Save output
    cv2.imwrite("dilated_image.jpg", dilated)

    print("Image dilation completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
