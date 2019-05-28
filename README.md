# Digital Image Processing
Assignment #1

## Task Description
For this assignment we were tasked with implementing two methods for zooming and shrinking an image using both linear and bilinear interpolation.

  ### This application requires **Python 3**

  ## Usage
   -  Install requirements: `pip install -r requirements.txt `
   -  `./dip_hw1_resize.py -i image-name -fx scalex -fy scaley -m method`
       - `image-name`: name of the image
       - `scalex`, `scaley`: scale to resize the image (eg. fx 0.5, fy 0.5 to make it half the original size)
       - `method`: "nearest_neightbor" or "bilinear"

  ### Example
    - ./dip_hw1_resize.py -i cell2.jpg -fx 0.75 -fy 0.75 -m nearest_neighbor
    - or
    - python dip_hw1_resize.py -i cell2.jpg -fx 0.75 -fy 0.75 -m nearest_neighbor

  Any output images are saved to "output/" folder

  Two images are provided for testing: cells.png and cell2.jpg

