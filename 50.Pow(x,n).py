class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
             return 1
        elif n < 0:
            x = 1 / x
            n = -n
        rs = 1

        while n > 0:
            if n % 2 == 1:
                rs *= x
            x *= x
            n //= 2

        return rs
