class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        num_str = str(num)
        for digit in num_str:
            digit = int(digit)
            if digit != 0 and num % digit == 0:
                count += 1
        return count
