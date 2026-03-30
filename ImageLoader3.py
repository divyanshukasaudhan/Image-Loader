import cv2
from PIL import Image, ImageTk
from tkinter import filedialog
import ImageProcessing4

def show_image(img,panel):

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(300,260))

    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    panel.config(image=img)
    panel.image = img

def upload_image(original_panel,preview_panel):

    path = filedialog.askopenfilename()

    if path:

        img = cv2.imread(path)

        ImageProcessing4.original_img = img
        ImageProcessing4.edited_img = img.copy()

        show_image(img,original_panel)
        show_image(img,preview_panel)