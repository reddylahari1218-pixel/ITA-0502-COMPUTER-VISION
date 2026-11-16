
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
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define four points in the original image
    pts1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Define four destination points
    pts2 = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    transformed = cv2.warpPerspective(
        img, matrix, (cols, rows)
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", transformed)

    # Save output
    cv2.imwrite("perspective_transformed.jpg", transformed)

    print("Perspective Transformation Completed Successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

root.destroy()
