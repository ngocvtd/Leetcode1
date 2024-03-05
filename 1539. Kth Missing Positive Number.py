class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2
            missing_acount = arr[m] - (m + 1)     # [1, 2, 3, 4, 5, 6. ... n]
                                                # [2, 3, 4, 7, 11] , k = 5  
            if missing_acount < k :
                l = m  + 1
            else:
                r = m - 1

        return l + k
