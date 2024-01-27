class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        rs = 0
        prev = 0
        cur = 0

        for c in s:
            cur = dict[c]
            rs += cur
            if prev < cur:
                rs = rs - prev * 2
            prev = cur
        return rs
