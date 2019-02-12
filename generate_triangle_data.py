import numpy as np
import cv2
import random
import math

pt_range_min = -50
pt_range_max = 50

x1 = 208
y1 = 104
x2 = 104
y2 = 338
x3 = 338
y3 = 338

img = np.zeros((416, 416, 3), np.uint8)
img[:] = (255, 255, 255)
pt1 = [x1, y1]
pt2 = [x2, y2]
pt3 = [x3, y3]
pts = np.array([pt1, pt2, pt3], np.int32)
img = cv2.polylines(img, [pts], True, (0, 0, 0), 3)
cv2.imwrite('./Images/003/triangle.jpg', img)


def get_cordinates_change():
    change = random.randint(pt_range_min, pt_range_max)
    return change


def get_cordinates_change_th():
    change = random.randint(0, 360)
    return change


# for i in range(100):
#     # Create a blank white image
#     img = np.zeros((128, 128, 3), np.uint8)
#     img[:] = (255, 255, 255)
#     pt1 = [x1 + get_cordinates_change(), y1 + get_cordinates_change()]
#     pt2 = [x2 + get_cordinates_change(), y2 + get_cordinates_change()]
#     pt3 = [x3 + get_cordinates_change(), y3 + get_cordinates_change()]
#     pts = np.array([pt1, pt2, pt3], np.int32)
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     img = cv2.polylines(img, [pts], True, (r, g, b), 3)
#     print(i, (r, g, b))
#     cv2.imwrite('./Images/003/triangle{}.jpg'.format(i), img)
def rotation(image, angle, r, g, b):
    center = tuple(np.array(image.shape[0:2]) / 2)
    rot_mat = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[0:2], flags=cv2.INTER_LINEAR, borderValue=(r, g, b))


for i in range(100):
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
    # x1 = x1 * math.cos(th) - y1 * math.sin(th)
    # x2 = x2 * math.cos(th) - y2 * math.sin(th)
    # x3 = x3 * math.cos(th) - y3 * math.sin(th)
    # y1 = x1 * math.sin(th) + y1 * math.cos(th)
    # y2 = x2 * math.sin(th) + y2 * math.cos(th)
    # y3 = x3 * math.sin(th) + y3 * math.cos(th)
    pt1 = [x1, y1]
    pt2 = [x2, y2]
    pt3 = [x3, y3]
    pts = np.array([pt1, pt2, pt3], np.int32)
    image = cv2.polylines(img, [pts], True, (r, g, b), 3)  # -1 if filled == 1 else 3)
    print(i, (r, g, b))
    th = get_cordinates_change_th()
    image = rotation(image, th, bg_r, bg_g, bg_r)
    cv2.imwrite('./Images/003/triangle{}.jpg'.format(i), image)
