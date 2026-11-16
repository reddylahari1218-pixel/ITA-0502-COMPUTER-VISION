
import cv2
import numpy as np
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

# Select an image
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read the input image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not selected or not found!")

else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert image to binary
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Opening morphological operation
    opening = cv2.morphologyEx(
        binary, cv2.MORPH_OPEN, kernel, iterations=1
    )

    # Display original image
    cv2.imshow("Original Image", img)

    # Display binary image
    cv2.imshow("Binary Image", binary)

    # Display opening image
    cv2.imshow("Opening Operation", opening)

    # Save output image
    cv2.imwrite("opening_image.jpg", opening)

    print("Opening Operation Completed Successfully!")
    print("Output saved as opening_image.jpg")

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

root.destroy()
