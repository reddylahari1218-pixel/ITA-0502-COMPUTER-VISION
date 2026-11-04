import cv2
from tkinter import Tk, filedialog

# Select an image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select your image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

root.destroy()

# Read the image
if not path:
    print("No image selected!")
else:
    img = cv2.imread(path)

    if img is None:
        print("Unable to read the image!")
    else:
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect edges using Canny
        edges = cv2.Canny(gray, 100, 200)

        # Display results
        cv2.imshow("Original Image", img)
        cv2.imshow("Canny Edge Detection", edges)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

