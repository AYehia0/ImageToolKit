Description:

    Image processing project to apply some preprocessing concepts using openCV
    library on nodejs.

    It will be a web page handled by express as backend.


ToDo:

    1- Create the server
    2- Create the routes : 

        - Single page to display images 
        - Maybe another page for circule detection using Hough Transform

    3- Process the image

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

            ---------

            * Edge detection filters

                - Laplacian filter
                - Vert Prewitt
                - Zero Cross
                - Gaussian filter
                - Horiz prewitt
                - Thicken
                - Vert sobel
                - Laplacian of Gaussian (log)
                - Skeleton 
                - Horiz 
                - Canny method
                - Thinning

        - Global Transformtion :
            
            * Line detection using Hough Transform
            * Circle detection using Hough Transform

            --------

            * Morphological operations
            (choosing type of kernel)

                - Dilation 
                - Erosion
                - 


    4- Display the image

    5- Save the image
