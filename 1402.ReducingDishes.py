class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse=True) 
        n = len(satisfaction)
        max_sum = 0
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += satisfaction[i]
            if prefix_sum <= 0:
                break
            max_sum += prefix_sum
        
        return max_sum
