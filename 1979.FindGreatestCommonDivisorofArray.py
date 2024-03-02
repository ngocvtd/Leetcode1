
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minimum = min(nums)
        maximum = max(nums)
        
        while minimum != 0:
            temp = minimum
            minimum = maximum % minimum
            maximum = temp
        
        return maximum
