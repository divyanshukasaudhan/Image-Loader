import cv2
from ImageLoader3 import show_image

original_img = None
edited_img = None

brightness_val = 100
contrast_val = 100
saturation_val = 100
blur_val = 0

def set_brightness(v):
    global brightness_val
    brightness_val = v

def set_contrast(v):
    global contrast_val
    contrast_val = v

def set_saturation(v):
    global saturation_val
    saturation_val = v

def set_blur(v):
    global blur_val
    blur_val = int(v)

def apply_adjustments(panel):

    global edited_img

    if original_img is None:
        return

    img = original_img.copy()

    b = brightness_val / 100
    img = cv2.convertScaleAbs(img,alpha=b,beta=0)

    c = contrast_val / 100
    img = cv2.convertScaleAbs(img,alpha=c,beta=0)

    s = saturation_val / 100
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv[:,:,1] = hsv[:,:,1] * s
    img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    if blur_val > 0:
        img = cv2.GaussianBlur(img,(blur_val*2+1,blur_val*2+1),0)

    edited_img = img

    show_image(img,panel)