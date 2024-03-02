class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        totalSum = sum(range(1, n+1))
        leftSum = 0
        rightSum = totalSum
        if n == 1 : return 1

        for i in range(1,n+1):
            rightSum -= i
            if rightSum == leftSum:
                return i
            leftSum += i
        return -1
            
