import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

if path:
    img = cv2.imread(path)

    if img is not None:
        blur = cv2.GaussianBlur(img, (15, 15), 0)

        cv2.imshow("Original Image", img)
        cv2.imshow("Gaussian Blur", blur)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unable to read image")
else:
    print("No image selected")
