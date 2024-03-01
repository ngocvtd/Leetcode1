class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for account in accounts:
            total = 0 
            for wealth in account:
                total += wealth  
            if total > max_wealth:
                max_wealth = total  
        
        return max_wealth
