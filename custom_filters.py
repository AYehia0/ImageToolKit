#Custom convolution filtering
import cv2
import numpy as np


# Custom convolution kernel
# Robertsedge operator
kernel_Roberts_x = np.array([
    [1, 0],
    [0, -1]
    ])
kernel_Roberts_y = np.array([
    [0, -1],
    [1, 0]
    ])
 # Sobel edge operator
kernel_Sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
kernel_Sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]])
 # Prewitt edge operator
kernel_Prewitt_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])
kernel_Prewitt_y = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]])

kernel_Laplacian_1 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]])
kernel_Laplacian_2 = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]])

 # Two convolution kernels do not have rotation invariance
kernel_Laplacian_3 = np.array([
    [2, -1, 2],
    [-1, -4, -1],
    [2, 1, 2]])
kernel_Laplacian_4 = np.array([
    [-1, 2, -1],
    [2, -4, 2],
    [-1, 2, -1]])
 # 5*5 LoG Convolution Template
kernel_LoG = np.array([
    [0, 0, -1, 0, 0],
    [0, -1, -2, -1, 0],
    [-1, -2, 16, -2, -1],
    [0, -1, -2, -1, 0],
    [0, 0, -1, 0, 0]])
 # convolution


def get_img(img_url):

    image = cv2.imread(img_url, 0)
    #image = cv2.resize(image,(800,800))

    return image

def Canny(image, k, t1, t2):

    img = cv2.GaussianBlur(image, (k, k), 0)
    canny = cv2.Canny(img, t1, t2)

    return canny


######## 

def prewitt_x(image):
    """Perform Prewitt in the X axis"""

    image = get_img(image)
    prewitt_x = cv2.filter2D(image, -1, kernel_Prewitt_x)

    return prewitt_x

def prewitt_y(image):
    """Perform Prewitt in the Y axis"""

    image = get_img(image)
    prewitt_y = cv2.filter2D(image, -1, kernel_Prewitt_y)

    return prewitt_y


######## 

def roberts_x(image):
    """Performs Robert in the X axis"""

    image = get_img(image)
    roberts_x = cv2.filter2D(image, -1, kernel_Roberts_x)

    return roberts_x

def roberts_y(image):
    """Performs Robert in the Y axis"""

    image = get_img(image)
    roberts_y = cv2.filter2D(image, -1, kernel_Roberts_y)

    return roberts_y
    
######## 

def sobel_x(image):
    """Sobel in X axis"""

    image = get_img(image)
    sobel_x = cv2.filter2D(image, -1, kernel_Sobel_x)

    return sobel_x


def sobel_y(image):
    """Sobel in Y axis"""

    image = get_img(image)
    sobel_y = cv2.filter2D(image, -1, kernel_Sobel_y)

    return sobel_y

#########

def laplacian(image, filter_=kernel_Laplacian_1):
    """Lap"""

    image = get_img(image)
    laplacian  = cv2.filter2D(image, -1, filter_)

    return laplacian

#########

def canny(image):
    """Canny using OpenCV"""

    image = get_img(image)
    canny = Canny(image,3,50,150)

    return canny
