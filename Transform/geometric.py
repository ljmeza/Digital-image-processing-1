import math

import numpy as np

import Transform.interpolation
class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by an angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""
        if (theta <0):
            theta=2+theta
        min_x = ((image.shape[0]-1) * math.cos(theta)) - (0 * math.sin(theta))
        max_x = (0 * math.cos(theta)) - ((image.shape[1]-1) * math.sin(theta))
        max_y = ((image.shape[0]-1) * math.sin(theta)) + ((image.shape[1]-1) * math.cos(theta))
        min_y = (0 * math.sin(theta)) + (0 * math.cos(theta))

        dim_x = round(max_x-min_x)
        dim_y = round(max_y-min_y)

        rotate_image = np.zeros((abs(dim_x)+1, abs(dim_y)+1), dtype = int)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                x1 = (x * math.cos(theta)) - (y * math.sin(theta))
                y1 = (x * math.sin(theta)) + (y * math.cos(theta))
                i=int(x1-min_x-1)
                j=int(y1-min_y)
                if((rotate_image.shape[0]*-1)<= i <0):
                   if(0<=j<rotate_image.shape[1]):
                     rotate_image[i, j] = image[x, y]





        return rotate_image

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by an angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: shape of the orginal image
                return the original image"""
        if (theta <0):
            theta=2+theta

        original_image = np.zeros(original_shape, dtype=int)
        for x in range(rotated_image.shape[0]):
            for y in range(rotated_image.shape[1]):
                i = x - origin[0]
                j = y - origin[1]
                x1 = (i * math.cos(theta)) + (j * math.sin(theta))
                y1 = (-i * math.sin(theta)) + (j * math.cos(theta))

                if 0 <= x1 < original_shape[0]:
                    if 0 <= y1 < original_shape[1]:
                        original_image[int(x1),int(y1)]= rotated_image[x,y]


        return original_image



    def rotate(self, image, theta, interpolation_type, origin):
        """Computes the forward rotated image by an angle theta using interpolation
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the original image"""
        geo=Geometric
        inter= Transform.interpolation.interpolation
        rotated_image=geo.forward_rotate(self,image,theta)
        original_shape=image.shape
        if (theta < 0):
            theta = 2 + theta
        if interpolation_type =="nearest_neighbor":
            for x in range(rotated_image.shape[0]):
                for y in range(rotated_image.shape[1]):
                    i = x - origin[0]
                    j = y - origin[1]
                    x1 = (i * math.cos(theta)) + (j * math.sin(theta))
                    y1 = (-i * math.sin(theta)) + (j * math.cos(theta))
                    if 0 <= x1 < original_shape[0]:
                        if 0 <= y1 < original_shape[1]:

                            rotated_image[x, y]=image[math.floor(x1), math.floor(y1)]
            return rotated_image
        if interpolation_type=="bilinear":
            for x in range(rotated_image.shape[0]):
                for y in range(rotated_image.shape[1]):
                    i = x - origin[0]
                    j = y - origin[1]
                    x1 = (i * math.cos(theta)) + (j * math.sin(theta))
                    y1 = (-i * math.sin(theta)) + (j * math.cos(theta))
                    if 0 <= x1 < original_shape[0]-1:
                        if 0 <= y1 < original_shape[1]-1:
                             rotated_image[x,y]=inter.bilinear_interpolation(self,x1,y1,image)
            return rotated_image


