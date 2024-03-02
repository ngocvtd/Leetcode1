class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        total_sum = 0

        for i in range(n):
            sub_sum = 0
            for length in range(1, n - i + 1,2):
                sub_sum +=sum(arr[i:i+length])
            total_sum  += sub_sum
        
        return total_sum
