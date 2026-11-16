
import cv2
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

# Select an image
image_path = filedialog.askopenfilename(
    title="Select Original Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read the original image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not selected or not found!")

else:
    # Create a copy of original image
    watermarked = img.copy()

    # Watermark text
    text = "WATERMARK"

    # Set font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 0, 255)
    thickness = 2

    # Get image dimensions
    height, width = img.shape[:2]

    # Set watermark position
    position = (width - 250, height - 30)

    # Insert watermark into image
    cv2.putText(
        watermarked,
        text,
        position,
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )

    # Display original image
    cv2.imshow("Original Image", img)

    # Display watermarked image
    cv2.imshow("Watermarked Image", watermarked)

    # Save watermarked image
    cv2.imwrite("watermarked_image.jpg", watermarked)

    print("Watermark inserted successfully!")
    print("Saved as watermarked_image.jpg")

    # Wait for key press
    cv2.waitKey(0)

    # Close windows
    cv2.destroyAllWindows()

root.destroy()
