import math

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    
        array_gcd = nums[0]
        for num in nums[1:]:
            array_gcd = gcd(array_gcd, num)
        
        return array_gcd == 1
