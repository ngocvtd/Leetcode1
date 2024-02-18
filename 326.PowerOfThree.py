class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1: 
            if n % 3 != 0:
                return False
            n /= 3
        if n == 1: 
            return True
