class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_types = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_types:
                count += 1
        
        return count 
