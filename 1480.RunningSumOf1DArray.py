class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0     
        rs = []      
        for num in nums:
            total += num
            rs.append(total)
        return rs
