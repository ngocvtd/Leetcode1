class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if(nums[j] - nums[i] == diff and nums[k] - nums[j] == diff and i < j and j < k):
                        count += 1

        return count
