class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        sum = arrivalTime + delayedTime
        if sum >= 24:
            sum -= 24
        return sum
