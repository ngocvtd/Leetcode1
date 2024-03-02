class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumElement = sum(nums)
        sumDigit = sum(int(digit) for num in nums for digit in str(num))

        return abs(sumElement - sumDigit)
        

            


