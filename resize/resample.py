import numpy as np
np.set_printoptions(threshold=np.inf)

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        # Write your code for nearest neighbor interpolation here
        print((fx, fy))

        (width, height) = image.shape
        (scaledWidth, scaledHeight) = (int(fy * width), int(fy * height))
        resampledImage = np.zeros((scaledWidth, scaledHeight), dtype=int)
        tempImage = np.resize(resampledImage, (width, height))
        print('temp image shape', tempImage.shape)
        print('original image shape', image.shape)
        for i in range(0, scaledWidth):
            for j in range(0, scaledHeight):
                print((i, j), (int(i / fx), int(j / fy)))
                (nx, ny) = (int(i / fx), int(j / fy))
                tempImage[i+1, j+1] = image[nx+1, ny+1]

        resampledImage = np.resize(tempImage, (scaledWidth, scaledHeight))
        return resampledImage

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        return image
