
import cv2
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
    height, width = img.shape[:2]

    # Select Region of Interest (ROI)
    x1 = width // 4
    y1 = height // 4
    x2 = 3 * width // 4
    y2 = 3 * height // 4

    # Crop the selected region
    roi = img[y1:y2, x1:x2]

    # Copy the ROI
    copied_roi = roi.copy()

    # Create a copy of original image
    result = img.copy()

    # Paste ROI at another location
    result[0:copied_roi.shape[0],
           0:copied_roi.shape[1]] = copied_roi

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Copied and Pasted Image", result)

    # Save output images
    cv2.imwrite("cropped_roi.jpg", roi)
    cv2.imwrite("roi_pasted.jpg", result)

    print("Image Cropping, Copying and Pasting Completed!")
    print("Output saved successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

root.destroy()
