import cv2
import numpy as np
from tkinter import Tk, filedialog

def analyze_histogram(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        hist = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX)
        hist = hist.flatten()

        hist_img = np.zeros((256, 256, 3), dtype=np.uint8)

        for x in range(256):
            y = int(hist[x])
            cv2.line(
                hist_img,
                (x, 255),
                (x, 255 - y),
                (255, 0, 0) if color == 'b'
                else (0, 255, 0) if color == 'g'
                else (0, 0, 255),
                1
            )

        cv2.imshow(channel_names[i] + " Histogram", hist_img)

    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

root.destroy()

if path:
    analyze_histogram(path)
else:
    print("No image selected!")
