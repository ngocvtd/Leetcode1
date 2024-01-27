class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = -2 ** 31
        max = 2 ** 31 - 1

        sign = 1 if x >= 0 else -1
        x = abs(x)

        rv_str = str(x)[::-1]
        rv = int(rv_str) * sign

        if rv <= min or rv >= max :
            return 0
        return rv

