import math



class interpolation:

    def linear_interpolation(self, start, end, x, intensity1, intensity2):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here

        total_len = end - start
        intensity = (((x - start) * intensity1) + ((end - x) * intensity2)) / total_len
        return intensity



    def bilinear_interpolation(self, x,y, image):
        inter=interpolation
        pt1I= image[(math.floor(x),math.floor(y))]
        pt2I = image[(math.floor(x),math.ceil(y))]
        pt3I= image[(math.ceil(x),math.floor(y))]
        pt4I=image[(math.ceil(x),math.ceil(y))]
        x1int=inter.linear_interpolation(self, math.floor(y), math.ceil(y),y,pt1I,pt2I)
        x2int=inter.linear_interpolation(self, math.floor(y), math.ceil(y),y,pt3I,pt4I)
        finalint=inter.linear_interpolation(self,math.floor(x),math.ceil(x),x,x1int,x2int)
        return finalint
        """Computes the bi linear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensities I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task



