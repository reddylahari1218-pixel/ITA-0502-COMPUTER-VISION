
import cv2
import numpy as np
from tkinter import Tk, filedialog

# Select an image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not selected or not found!")

else:
    # Convert image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert grayscale image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(
        gray, 2, 3, 0.04
    )

    # Dilate corner points
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Display original and detected images
    original = cv2.imread(image_path)

    cv2.imshow("Original Image", original)
    cv2.imshow("Harris Corner Detection", img)

    # Save output image
    cv2.imwrite("harris_corners.jpg", img)

    print("Harris Corner Detection Completed Successfully!")
    print("Output saved as harris_corners.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

root.destroy()
