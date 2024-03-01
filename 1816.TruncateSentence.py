class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr = s.split(" ")
        rs = []
        for i in range(k):
            rs.append(arr[i])
        result = ' '.join(rs)
        return result
