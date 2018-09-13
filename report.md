###Raul Rios

#Assignment 1

####Task Description
For this assignment we have been tasked to implement two methods for zooming and shrinking an image using both linear and bilinear interpolation.  

####Nearest Neighbor Interpolation

This first part of the task was accomplished by first implementing the functions, `nearest_neighbor` and `linear_interpolation`, in **resample.py** and **interpolation.py** respectively. To begin, I obtained the dimensions of the original image using the `shape` property which returned the width and height of the image. These dimensions were then scaled using the scaling factors passed through to `fx` and `fy` and multiplying them by the original image's `width` and `height` respectively. A new image for the representation of the original image was created using the `np.zeros` function by passing the tuple `(scaledWidth, scaledHeight)` to set the dimension of the resized image. I then iterated through each pixel of the resized image `left -> right, top -> bottom`. At each position, the `x` and `y` values are divided by the scaling factors `fx` and `fy` in order to find the location of the corresponding pixel in the original image, namely `nx` and `ny`. 

The `linear_interpolation` function in **interpolation.py** is then called with three parameters. The first is the location of the current image and the intensity value at that location. The second is the location of the pixel value to the right along with its intensity at that location in the original image. The third parameter is the location of the unknown value that needs the intensity value found. What this function does is return the value of the linear interpolation equation `I = I1(x2 - x)/(x2 - x1) + I2(x - x1)/(x2 - x1)` which gives the appropriate intensity value given the parameters previously described.  

Once all the pixel locations of the resample image have been assigned the corresponding intensity values, the image is returned.


####Bilinear Interpolation

The second part of the task was accomplished by implementing the functions name `bilinear_interpolation` in both **resample.py** and **interpolation.py**. This was done in a very similar fashion as for the `nearest_neighbor` method only that now instead of just finding one nearest neighbor, three additional neighbors were identified. Keeping in mind that `nx` and `ny` are the current location of the original image, the neighbors are `(nx, ny+1), (nx+1, ny), and (nx+1, ny+1)`. These 4 points are passed onto the `bilinear_interpolation` function along with the location of the unknown intensity value. 

In the `bilinear_interpolation` function the `linear_interpolation` function is reused three times. The first time is used the calculate the intensity value between the first two points i.e. `(nx, ny) and (nx, ny+1)`. The second time, the function is used to calculate the intensity value between the third and fourth points i.e. `(nx+1, ny), and (nx+1, ny+1)`. In the third call to the function, the intensity values found in the previous two calculations along with their corresponding x values are used to interpolate and find the correct intensity value to return. 

####Conclusion

On the surface, theoretically speaking it seems that bilinear interpolation is a method that produces a higher quality resizing of any image. However, throughout my attempts of both scaling up and down an image, I was not able to see a clear difference between the two. 
  

