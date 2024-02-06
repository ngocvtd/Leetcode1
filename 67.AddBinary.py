class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = int(a,2)
        b1 = int(b,2)

        ab = a1 + b1
        rs = bin(ab)[2:]
        return rs
