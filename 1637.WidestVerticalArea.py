class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sort_points = sorted(points, key= lambda x : x[0])

        max_rs = 0
        for i in range(1, len(points)):
            width = sort_points[i][0] - sort_points[i - 1][0]
            max_rs = max(max_rs, width)

        return max_rs
