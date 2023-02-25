import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
blank_image = np.zeros((1920, 1080, 3), np.uint8)
blank_image.fill(255)
cv2.imwrite(f'image.jpg', blank_image)
