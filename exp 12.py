
import cv2
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

# Select image from laptop
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read the selected image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not selected or not found!")

else:
    # Rotate image 270 degrees clockwise
    rotated_image = cv2.rotate(
        img, cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    # Display original image
    cv2.imshow("Original Image", img)

    # Display rotated image
    cv2.imshow("270 Degree Clockwise Rotated Image", rotated_image)

    # Save rotated image
    cv2.imwrite("rotated_270_image.jpg", rotated_image)

    print("270 Degree Clockwise Rotation Completed Successfully!")

    # Wait for key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

root.destroy()
