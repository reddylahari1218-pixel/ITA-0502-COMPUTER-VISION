
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

    # Apply Sobel filter in X direction
    sobel_x = cv2.Sobel(
        gray, cv2.CV_64F, 1, 0, ksize=3
    )

    # Apply Sobel filter in Y direction
    sobel_y = cv2.Sobel(
        gray, cv2.CV_64F, 0, 1, ksize=3
    )

    # Convert results to uint8
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)

    # Combine X and Y gradients
    sobel_result = cv2.addWeighted(
        sobel_x, 0.5, sobel_y, 0.5, 0
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)
    cv2.imshow("Sobel Edge Detection", sobel_result)

    # Save output image
    cv2.imwrite("sobel_output.jpg", sobel_result)

    print("Sobel Algorithm Completed Successfully!")
    print("Output saved as sobel_output.jpg")

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

root.destroy()
