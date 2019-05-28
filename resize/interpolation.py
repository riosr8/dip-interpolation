class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for linear interpolation here

        return (pt1[1] * ((pt2[0] - unknown) / (pt2[0] - pt1[0]))) + (pt2[1] * ((unknown - pt1[0]) / (pt2[0] - pt1[0])))

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        i1 = self.linear_interpolation([pt1[0][1], pt1[1]], [pt2[0][1], pt2[1]], unknown[1])
        i2 = self.linear_interpolation([pt3[0][1], pt3[1]], [pt4[0][1], pt4[1]], unknown[1])

        return self.linear_interpolation([pt1[0][0], i1], [pt3[0][0], i2], unknown[0])
