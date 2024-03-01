class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        mid = len(nums) // 2
        x = nums[:mid]
        y = nums[mid:]

        shuffle = []
        for i in range(n):
            shuffle.append(x[i])
            shuffle.append(y[i])
        
        return shuffle
