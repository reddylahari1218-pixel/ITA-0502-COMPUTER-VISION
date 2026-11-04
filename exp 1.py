import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select an image",
    initialdir="C:/Users/HP/Desktop",
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

root.destroy()

print("Image path:", path)

if path:
    img = cv2.imread(path)

    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original Image", img)
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Unable to read image")
else:
    print("No image selected")
