
import cv2

# Read the input image
img = cv2.imread("image.jpg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Rotate image 90 degrees clockwise
    rotated_image = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display original image
    cv2.imshow("Original Image", img)

    # Display rotated image
    cv2.imshow("90 Degree Clockwise Rotated Image", rotated_image)

    # Save rotated image
    cv2.imwrite("rotated_image.jpg", rotated_image)

    print("Image rotated successfully!")

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
