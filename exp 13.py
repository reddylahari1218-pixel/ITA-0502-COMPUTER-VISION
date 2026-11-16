
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
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define three original points
    pts1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # Define three destination points
    pts2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine transformation
    transformed = cv2.warpAffine(
        img, matrix, (cols, rows)
    )

    # Display original image
    cv2.imshow("Original Image", img)

    # Display transformed image
    cv2.imshow("Affine Transformed Image", transformed)

    # Save output image
    cv2.imwrite("affine_transformed.jpg", transformed)

    print("Affine Transformation Completed Successfully!")
    print("Output saved as affine_transformed.jpg")

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()

root.destroy()
