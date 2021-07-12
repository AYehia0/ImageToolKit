This is an Image Processing ToolKit, using PyQt for the frontend and openCV for backend.

## Feature List 
Those with * after either don't work, or not yet implemented.

    Process the image

        - Converting : 
            * Default colour 
            * Gray Color
        - Point Transformation : 
            * Brightness adjustments
            * Contrast adjustments
            * Showing histogram
            * Histogram Equalization
        - Local Transformation : 
            * Low pass filter
            * High pass filter
            * Median filter(grey image)
            * Averaging filter
            * Edge detection filters
                - Laplacian filter
                - Vert Prewitt
                - Zero Cross
                - Gaussian filter
                - Horiz prewitt *
                - Thicken *
                - Vert sobel
                - Laplacian of Gaussian (log)
                - Skeleton *
                - Horiz *
                - Canny method
                - Thinning *
        - Global Transformtion :   
            * Line detection using Hough Transform
            * Circle detection using Hough Transform
            * Morphological operations
            (choosing type of kernel)*
                - Dilation 
                - Erosion
    Display the image
    Save the image *

## Bugs 

- Line detection using Hough Transform might not work properly 
- Program might crash while adding noise 
- Can't save/export the image [didn't add that feature yet]
- you have to click the radio button to refresh, doesn't support automatic refresh
- Brightness and Contrast Adjustment, shows negative images. [was laze to fix]
- Thining, Thicking and Skeleton don't work. [didn't add]

## Important Notes

- This is a beta version, with a lot of code faults, need to be refactored. 
- The GUI is compact, i was busy doing the backend rather than fixing the frontend.
- This may work on linux, but i didn't test.

## ScreenShots
