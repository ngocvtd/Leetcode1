class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
         n = len(nums)
         """
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n

    # Tính tổng trái tại mỗi vị trí
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]

    # Tính tổng phải tại mỗi vị trí
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

    # Tính giá trị tại mỗi vị trí của mảng answer
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])

        return answer
