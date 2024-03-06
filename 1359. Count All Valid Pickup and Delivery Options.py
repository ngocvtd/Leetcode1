class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        rs = 1
        for i in range(1, n + 1):
            rs = (rs * i * ( i * 2 - 1)) % MOD
        
        return rs
