class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l , r = 1, num

        while l <= r:
            m = l + (r - l) // 2
            square = m * m
            if square == num:
                return True
            elif square < num:
                l = m + 1
            elif square > num:
                r = m -1
        return False
