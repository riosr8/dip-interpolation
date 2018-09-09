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

        (width, height) = image.shape
        (scaledWidth, scaledHeight) = (int(fx * width), int(fy * height))
        resampledImage = np.zeros((scaledWidth, scaledHeight), dtype=int)

        for i in range(0, scaledWidth):
            for j in range(0, scaledHeight):
                (nx, ny) = (self.linear_interpolation(i, fx), self.linear_interpolation(j, fy))
                resampledImage[i, j] = image[nx, ny]

        return resampledImage

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        (width, height) = image.shape
        (scaledWidth, scaledHeight) = (int(fy * width), int(fy * height))
        resampledImage = np.zeros((scaledWidth, scaledHeight), dtype=int)

        # for i in range(0, scaledWidth):
        #     for j in range(0, scaledHeight):
        #

        return image

    def linear_interpolation(self, p, scale):
        interpolatedValue = int(p / scale)
        return interpolatedValue


