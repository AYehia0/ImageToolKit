"""
Backend for the GUI app:
    - Converting the Image colors 

"""

import cv2
import numpy as np
import math
import skimage

MIN_BRIGHTNESS= 255
MIN_contrast = 127

MAX_BRIGHTNESS = 510
MAX_contrast = 254

def read_img(path):
    """return the read image"""

    return cv2.imread(path)

def test(img):
    """Testing the img"""

    cv2.imwrite('wtf.png', img)
    cv2.imshow('test', img)


def conv_grey(img_path):
    """Convert Image from default(RGB) to grey scale"""

    image = read_img(img_path)
    grey  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return grey 

def controller(img, brightness=255,
               contrast=127):
    
    brightness = int((brightness - 0) * (255 - (-255)) / (MAX_BRIGHTNESS - 0) + (-255))
  
    contrast = int((contrast - 0) * (127 - (-127)) / (MAX_contrast - 0) + (-127))
  
    if brightness != 0:
  
        if brightness > 0:
  
            shadow = brightness
            max = 255
  
        else:
            shadow = 0
            max = 255 + brightness
  
        al_pha = (max - shadow) / 255
        ga_mma = shadow
  
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)
  
    else:
        cal = img
  
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
  
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)
  
    # # putText renders the specified text string in the image.
    # cv2.putText(cal, 'B:{},C:{}'.format(brightness,
    #                                     contrast), (10, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
  
    return cal
  
def histogram_eq(img_path):
    """Return the img after doing histogram equalization"""

    img = cv2.imread(img_path, 0)

    eq = cv2.equalizeHist(img)

    return eq

 #Add noise to the image
def random_noise(img_path):
    img = cv2.imread(img_path)
    
    noisy_image = skimage.util.random_noise(img, mode='gaussian')
    
    return noisy_image

def s_and_p(img_path):
    img = cv2.imread(img_path)
    
    noisy_image = skimage.util.random_noise(img, mode='s&p')
    
    return noisy_image
   
def poisson(img_path):
    img = cv2.imread(img_path)
    
    noisy_image = skimage.util.random_noise(img, mode='poisson')
    
    return noisy_image
   
def lp_filter(img_path):
    """Using boxFilter as a low pass filter"""

    # reading the img
    img = cv2.imread(img_path, 1)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    box_filter = cv2.boxFilter(img, -1, (15, 15))

    return box_filter


def hp_filter(img_path):
    """Using Img - The GaussianBlur to show the edges"""

    # helper function
    def hp(img, sigma=3):
        return img - cv2.GaussianBlur(img, (0, 0), sigma) + 127

    img = read_img(img_path)

    mod_hp = hp(img) 

    return mod_hp

def median_filter(img_path):
    """Using the in-built medianBlur in the openCV"""

    img = read_img(img_path)

    median = cv2.medianBlur(img, 5)

    return median


def avg_filter(img_path):
    """Using the blur in the openCV to apply avareging filter"""
    
    img = read_img(img_path)

    avg = cv2.blur(img, (5, 5))

    return avg

def log_filter(img_path):
    """Applying lap filter"""

    # reading 
    img = read_img(img_path)


    # gray scale 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Removing noise
    img = cv2.GaussianBlur(img, (3,3), 0)

    # convolute with proper kernels 
    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    return laplacian

def sobel_filter(img_path, x=1, y=1):
    # reading 
    img = read_img(img_path)


    # gray scale 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # x and y
    sobel = cv2.Sobel(img, cv2.CV_64F, x, y, ksize=5)

    return sobel

def circle_hough(img_path):
    # reading 
    img = read_img(img_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.medianBlur(gray, 5)
    
    cimg = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,120, param1=100, param2=30, minRadius=0, maxRadius=0)
     
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)

            # center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)

    
    return img


def line_hough(img_path):

    # reading 
    img = read_img(img_path)

    # gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
 
    #  Standard Hough Line Transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
  
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
            x1 = int(x0 + 1000 * (-b))
            # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
            y1 = int(y0 + 1000 * (a))
            # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
            x2 = int(x0 - 1000 * (-b))
            # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    
    return img

def erosion(img_path):
    # reading 
    img = read_img(img_path)

    # gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    for i in range(0, 3):
        eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    
    return eroded

def dilation(img_path):
    # reading 
    img = read_img(img_path)

    # gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    for i in range(0, 3):
        dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)

    
    return dilated

def open_(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
    kernal = np.ones((5,5), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

    return opening

def close_(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
    kernal = np.ones((5,5), np.uint8)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

    return closing

# #Read picture
# img = cv2.imread('cat.jpg', 0)
# #Add Gaussian noise
# img1 = random_noise(img,'gaussian', mean=0.1,var=0.01)
# img1 = np.uint8(img1*255)
# #
# cv2.imshow('img', img)
# cv2.imshow('img1', img1)
