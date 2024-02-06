class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rs = 0
        for num in nums :
            rs ^= num
        return rs
