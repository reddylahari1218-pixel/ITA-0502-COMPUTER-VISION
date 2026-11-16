
import cv2
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
    print("Error: Image not found!")
else:
    # Resize image to bigger size
    bigger = cv2.resize(img, None, fx=2, fy=2,
                        interpolation=cv2.INTER_LINEAR)

    # Resize image to smaller size
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5,
                          interpolation=cv2.INTER_AREA)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display bigger image
    cv2.imshow("Bigger Image", bigger)

    # Display smaller image
    cv2.imshow("Smaller Image", smaller)

    # Save resized images
    cv2.imwrite("bigger_image.jpg", bigger)
    cv2.imwrite("smaller_image.jpg", smaller)

    print("Image scaling completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
