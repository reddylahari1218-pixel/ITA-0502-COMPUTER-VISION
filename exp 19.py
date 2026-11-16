
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

# Read the image
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

    # Apply erosion operation
    erosion = cv2.erode(
        binary, kernel, iterations=1
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Erosion Image", erosion)

    # Save erosion output
    cv2.imwrite("erosion_image.jpg", erosion)

    print("Erosion Operation Completed Successfully!")
    print("Output saved as erosion_image.jpg")

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

root.destroy()
