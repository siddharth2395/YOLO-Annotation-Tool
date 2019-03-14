import numpy as np
import cv2
import random

pt_range_min_circle = -16
pt_range_max_circle = 48

pt_range_min_square = -52
pt_range_max_square = 52


def get_cordinates_change_square():
    change = random.randint(pt_range_min_square, pt_range_max_square)
    return change


def get_cordinates_change_circle():
    change = random.randint(pt_range_min_circle, pt_range_max_circle)
    return change


def random_light():
    return random.randint(0, 128), random.randint(0, 128), random.randint(0, 128)


def random_dark():
    return random.randint(128, 256), random.randint(128, 256), random.randint(128, 256)


def get_inside_square_cordinates(x, y, R):
    change = (R * 40) / 100 if R < 416 / 2 else (R * 20) / 100
    print(R, change)
    R = int(R - change * 1.2)
    x1, y1 = x + R, y - R
    x2, y2 = x - R, y + R
    return x1, y1, x2, y2


def get_outside_square_cordinates(x, y, R):
    change = (R * 80) / 100 if R < 416 / 8 else (R * 65) / 100 if R < 416 / 6 else (R * 50) / 100 if R < 416 / 3 else (R * 30) / 100 if R < 416 / 2 else (R * 20) / 100
    # print(R, change)
    R = int(R + change)
    x1, y1 = x - R, y + R
    x2, y2 = x + R, y - R
    return x1, y1, x2, y2


def square_in_circle():
    x = y = 208
    R = 128

    x1 = 78
    y1 = 78
    x2 = 338
    y2 = 338
    for i in range(1000):
        # Create a blank white image
        light_bg = random.randint(0, 1)
        if light_bg == 0:
            img = np.zeros((416, 416, 3), np.uint8)
            bg_r, bg_g, bg_b = random_dark()
            img[:] = ((bg_r, bg_g, bg_b))
            r, g, b = random_light()
        else:
            img = np.zeros((416, 416, 3), np.uint8)
            bg_r, bg_g, bg_b = random_light()
            img[:] = ((bg_r, bg_g, bg_b))
            r, g, b = random_dark()
        filled = random.randint(0, 1)
        ix = x + get_cordinates_change_circle()
        iy = y + get_cordinates_change_circle()
        iR = R + get_cordinates_change_circle()
        x1, y1, x2, y2 = get_inside_square_cordinates(ix, iy, iR)
        img = cv2.circle(img, (ix, iy), iR, (r, g, b), -1 if filled == 1 else 3)

        if filled == 1:
            img = cv2.rectangle(img, (x1, y1), (x2, y2), (abs(255 - r), abs(255 - g), abs(255 - b)),
                                -1 if filled == 1 else 3)
        else:
            if light_bg == 0:
                r, g, b = random_light()
            else:
                r, g, b = random_dark()

            img = cv2.rectangle(img, (x1, y1), (x2, y2), (r, g, b),
                                -1 if filled == 1 else 3)
        print(i, (r, g, b))

        cv2.imwrite('../Images/mixed/{}.jpg'.format(i), img)


def circle_in_square():
    global pt_range_min_circle, pt_range_max_circle
    pt_range_min_circle = -50
    pt_range_max_circle = 30

    x = y = 208
    R = 80

    x1 = 78
    y1 = 78
    x2 = 338
    y2 = 338
    for i in range(1000):
        # Create a blank white image
        light_bg = random.randint(0, 1)
        if light_bg == 0:
            img = np.zeros((416, 416, 3), np.uint8)
            bg_r, bg_g, bg_b = random_dark()
            img[:] = ((bg_r, bg_g, bg_b))
            r, g, b = random_light()
        else:
            img = np.zeros((416, 416, 3), np.uint8)
            bg_r, bg_g, bg_b = random_light()
            img[:] = ((bg_r, bg_g, bg_b))
            r, g, b = random_dark()
        filled = random.randint(0, 1)
        ix = x + get_cordinates_change_circle()
        iy = y + get_cordinates_change_circle()
        iR = R + get_cordinates_change_circle()
        x1, y1, x2, y2 = get_outside_square_cordinates(ix, iy, iR)
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (r, g, b),
                            -1 if filled == 1 else 3)
        if filled == 1:
            img = cv2.circle(img, (ix, iy), iR, (abs(255 - r), abs(255 - g), abs(255 - b)), -1 if filled == 1 else 3)
        else:
            if light_bg == 0:
                r, g, b = random_light()
            else:
                r, g, b = random_dark()
            img = cv2.circle(img, (ix, iy), iR, (r, g, b), -1 if filled == 1 else 3)

        print(i, (r, g, b))

        cv2.imwrite('../Images/mixed/{}.jpg'.format(1000 + i), img)


square_in_circle()

circle_in_square()
