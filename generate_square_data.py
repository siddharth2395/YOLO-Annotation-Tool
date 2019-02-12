import numpy as np
import cv2
import random

pt_range_min = -52
pt_range_max = 52

x1 = 78
y1 = 78
x2 = 338
y2 = 338

img = np.zeros((416, 416, 3), np.uint8)
img[:] = (255, 255, 255)

img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 3)
cv2.imwrite('./Images/001/square.jpg', img)


def get_cordinates_change():
    change = random.randint(pt_range_min, pt_range_max)
    return change


for i in range(1000):
    # Create a blank white image
    light_bg = random.randint(0, 1)
    if light_bg == 0:
        img = np.zeros((416, 416, 3), np.uint8)
        bg_r = random.randint(128, 256)
        bg_g = random.randint(128, 256)
        bg_b = random.randint(128, 256)
        img[:] = ((bg_r, bg_g, bg_b))
        r = random.randint(0, 128)
        g = random.randint(0, 128)
        b = random.randint(0, 128)
    else:
        img = np.zeros((416, 416, 3), np.uint8)
        bg_r = random.randint(0, 128)
        bg_g = random.randint(0, 128)
        bg_b = random.randint(0, 128)
        img[:] = ((bg_r, bg_g, bg_b))
        r = random.randint(128, 256)
        g = random.randint(128, 256)
        b = random.randint(128, 256)
    filled = random.randint(0, 1)
    img = cv2.rectangle(img, (x1 + get_cordinates_change(), y1 + get_cordinates_change()),
                        (x2 + get_cordinates_change(), y2 + get_cordinates_change()), (r, g, b),
                        -1 if filled == 1 else 3)
    print(i, (r, g, b))
    cv2.imwrite('./Images/001/square{}.jpg'.format(i), img)
