"""
Backend for the GUI app:
    - Converting the Image colors 

"""
import cv2

def conv_grey(img_path):
    """Convert Image from default(RGB) to grey scale"""

    image = cv2.imread(img_path)
    grey  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return grey 
