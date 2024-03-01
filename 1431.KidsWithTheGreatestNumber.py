class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        rs = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                rs.append(True)
            else:
                rs.append(False)
        return rs
