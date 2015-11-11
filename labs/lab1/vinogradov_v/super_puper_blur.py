import cv2
import numpy as np
import sys

usage_str = "super_puper_blur.py <img_path> <kernel_coef>\n\
img_path - path to the image\n\
kernel_coef - an integer value that represent kernel size coefficient"
k_size_denom = 10

def blur_image(img_src, kernel_coef):
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)

    img_edges = cv2.Canny(img_gray, 100, 200)
    img_edges = cv2.bitwise_not(img_edges)

    img_distance = cv2.distanceTransform(img_edges, cv2.DIST_L2, 3)

    img_integral = cv2.integral(img_src)

    img_dst = np.zeros(img_src.shape, img_src.dtype)
    for y in range(0, img_src.shape[0]):
        for x in range(0, img_src.shape[1]):
            # Calculate kernel size
            ksize = kernel_coef * img_distance[y, x]
            # Find kenrel borders
            start_x = (int)(max(0, x - ksize / 2))
            start_y = (int)(max(0, y - ksize / 2))
            end_x = (int)(min(x + ksize / 2, img_src.shape[1] - 1))
            end_y = (int)(min(y + ksize / 2, img_src.shape[0] - 1))
            # Get sum of pixels in the kernel region
            sum_px = img_integral[end_y + 1, end_x + 1] - img_integral[start_y, end_x + 1] - \
                img_integral[end_y + 1, start_x] + img_integral[start_y, start_x]
            box_count = (end_y - start_y + 1) * (end_x - start_x + 1)
            # Put new values into destination image
            if (box_count > 1):
                img_dst[y, x] = (sum_px) / box_count
            else:
                img_dst[y, x] = img_gray[y, x]

    return img_dst

def print_usage():
    print usage_str
    exit()

if __name__ == '__main__':
    if (len(sys.argv) < 3):
        print_usage()

    image_name = sys.argv[1]
    k_coef = int(sys.argv[2])
    if (k_coef == 0):
        print_usage()
    k = k_coef / k_size_denom

    img_src = cv2.imread(image_name)

    img_blured = blur_image(img_src, k)

    cv2.imshow("img_src", img_src)
    cv2.imshow("img_dst", img_blured)
    cv2.waitKey()
    cv2.destroyAllWindows()
