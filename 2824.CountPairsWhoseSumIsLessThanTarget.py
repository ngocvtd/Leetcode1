class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        l = 0
        r = len(nums) - 1

        while l < r :
            if nums[l] + nums[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1
        
        return count
        
