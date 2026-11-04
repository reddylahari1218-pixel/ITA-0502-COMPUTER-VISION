import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select your image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

if path:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Unable to read image!")
    else:
        equalized = cv2.equalizeHist(img)

        cv2.imshow("Original Grayscale Image", img)
        cv2.imshow("Histogram Equalized Image", equalized)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("No image selected!")
