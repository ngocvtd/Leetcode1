class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rv = str(x)[::-1]
        num_rv = int(rv)

        return num_rv == x
