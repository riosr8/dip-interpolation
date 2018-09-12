import numpy as np
import math
import resize.interpolation
np.set_printoptions(threshold=np.inf)

class resample:

    def __init__(self):
        self.inter = resize.interpolation.interpolation()

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

        for x in range(0, scaledWidth):
            for y in range(0, scaledHeight):
                nx = int(x / fx)
                ny = int(y / fy)
                if (nx + 1) > width - 1:
                    nx = width - 2
                if (ny + 1) > height - 1:
                    ny = height - 2
                resampledImage[x, y] = self.inter.linear_interpolation([ny, image[nx, ny]], [ny+1, image[nx, ny+1]], y/fy)

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

        for x in range(0, scaledWidth):
            for y in range(0, scaledHeight):
                nx = math.floor(x / fx)
                ny = math.floor(y / fy)
                if (nx + 1) > width - 1:
                    nx = width - 2
                if (ny + 1) > height - 1:
                    ny = height - 2

                n1 = (nx, ny)
                n2 = (nx, ny+1)
                n3 = (nx+1, ny)
                n4 = (nx+1, ny+1)

                resampledImage[x, y] = self.inter.bilinear_interpolation([n1, image[n1]], [n2, image[n2]], [n3, image[n3]],[n4, image[n4]], [x/fx, y/fy])

        return resampledImage





