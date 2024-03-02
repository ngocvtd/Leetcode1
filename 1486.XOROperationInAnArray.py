class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [start + 2 * i for i in range(n)]  # Tạo mảng nums theo công thức nums[i] = start + 2 * i
        result = 0
        for num in nums:
            result ^= num  # Thực hiện phép XOR với từng phần tử num

        return result
