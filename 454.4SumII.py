class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        rs = defaultdict(int)
        count = 0

        for num1 in nums1:
            for num2 in nums2:
                rs[num1 + num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                tagert = 0 - (num3 + num4)
                count += rs[tagert]
        
        return count
