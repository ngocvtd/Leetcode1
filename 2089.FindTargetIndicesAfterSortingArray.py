class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        rs = []
        for i in range(len(nums)):
            if nums[i] == target:
                rs.append(i)
        
        return rs
