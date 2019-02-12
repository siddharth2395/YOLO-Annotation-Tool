# circle
import numpy as np
import cv2
import random

pt_range_min = -8
pt_range_max = 8

x = y = 64
r = 28
img = np.zeros((128, 128, 3), np.uint8)
img[:] = (255, 255, 255)

img = cv2.circle(img, (x, y), r, (0, 0, 0), 3)
cv2.imwrite('./shape_data/test/circle/base_circle.png', img)


def get_cordinates_change():
    change = random.randint(pt_range_min, pt_range_max)
    return change


for i in range(125):
    print(i)
    # Create a blank white image
    img = np.zeros((128, 128, 3), np.uint8)
    img[:] = (255, 255, 255)
    img = cv2.circle(img, (x + get_cordinates_change(), y + get_cordinates_change()), r + get_cordinates_change(),
                     (0, 0, 0), 3)
    cv2.imwrite('./shape_data/test/circle/circle{}.png'.format(i), img)

# square
import numpy as np
import cv2
import random

pt_range_min = -25
pt_range_max = 16

x1 = 32
y1 = 32
x2 = 96
y2 = 96

img = np.zeros((128, 128, 3), np.uint8)
img[:] = (255, 255, 255)

img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 3)
cv2.imwrite('./shape_data/test/square/base_square.png', img)


def get_cordinates_change():
    change = random.randint(pt_range_min, pt_range_max)
    return change


for i in range(125):
    print(i)
    # Create a blank white image
    img = np.zeros((128, 128, 3), np.uint8)
    img[:] = (255, 255, 255)
    img = cv2.rectangle(img, (x1 + get_cordinates_change(), y1 + get_cordinates_change()),
                        (x2 + get_cordinates_change(), y2 + get_cordinates_change()), (0, 0, 0), 3)
    cv2.imwrite('./shape_data/test/square/square{}.png'.format(i), img)

# triangle
import numpy as np
import cv2
import random

pt_range_min = -25
pt_range_max = 16

x1 = 64
y1 = 32
x2 = 32
y2 = 96
x3 = 96
y3 = 96

img = np.zeros((128, 128, 3), np.uint8)
img[:] = (255, 255, 255)
pt1 = [x1, y1]
pt2 = [x2, y2]
pt3 = [x3, y3]
pts = np.array([pt1, pt2, pt3], np.int32)
img = cv2.polylines(img, [pts], True, (0, 0, 0), 3)
cv2.imwrite('./shape_data/test/triangle/base_triangle.png', img)


def get_cordinates_change():
    change = random.randint(pt_range_min, pt_range_max)
    return change


for i in range(125):
    print(i)
    # Create a blank white image
    img = np.zeros((128, 128, 3), np.uint8)
    img[:] = (255, 255, 255)
    pt1 = [x1 + get_cordinates_change(), y1 + get_cordinates_change()]
    pt2 = [x2 + get_cordinates_change(), y2 + get_cordinates_change()]
    pt3 = [x3 + get_cordinates_change(), y3 + get_cordinates_change()]
    pts = np.array([pt1, pt2, pt3], np.int32)
    img = cv2.polylines(img, [pts], True, (0, 0, 0), 3)
    cv2.imwrite('./shape_data/test/triangle/triangle{}.png'.format(i), img)
