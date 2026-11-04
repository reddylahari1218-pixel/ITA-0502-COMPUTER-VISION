import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")]
)
root.destroy()

if path:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Unable to read image!")
    else:
        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT, (5, 5)
        )

        eroded = cv2.erode(img, kernel, iterations=1)

        cv2.imshow("Original Image", img)
        cv2.imshow("Eroded Image", eroded)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("No image selected!")
