"""
Backend for the GUI app:
    - Converting the Image colors 

"""
import cv2



MIN_BRIGHTNESS= 255
MIN_contrast = 127

MAX_BRIGHTNESS = 510
MAX_contrast = 254

def read_img(path):
    """return the read image"""

    return cv2.imread(path)



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
