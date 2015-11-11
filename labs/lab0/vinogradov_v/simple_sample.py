import cv2
import numpy as np
import sys

usage_str = "super_puper_blur.py <img_path> <kernel_coef>\n\
img_path - path to the image"

if (len(sys.argv) < 2):
    print usage_str
    exit()

img_src = cv2.imread(sys.argv[1])

img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

img_dst_eq_hist = cv2.equalizeHist(img_gray)

img_blur = cv2.GaussianBlur(img_src, ksize=(5, 5), sigmaX=2, sigmaY=2)

ret, img_thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
img_morph = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

img_edges = cv2.Canny(img_gray, 100, 200)

cv2.imshow("img_src", img_src)
cv2.imshow("img_blur", img_blur)
cv2.imshow("img_dst_eq_hist", img_dst_eq_hist)
cv2.imshow("img_thresh", img_thresh)
cv2.imshow("img_morph", img_morph)
cv2.imshow("img_edges", img_edges)
cv2.waitKey()
cv2.destroyAllWindows()
