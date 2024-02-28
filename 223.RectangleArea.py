class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        max_x1 = max(ax1, bx1)
        max_y1 = max(ay1, by1)

        min_x2 = min(ax2, bx2)
        min_y2 = min(ay2, by2)

        width = min_x2 - max_x1
        height = min_y2 - max_y1

        s1 = (ax2 - ax1) * (ay2 - ay1)
        s2 = (bx2 - bx1) * (by2 - by1)
        s3 = width * height

        if max_x1 > min_x2 or max_y1 > min_y2:
            return s1 + s2
        return s1 + s2 - s3
