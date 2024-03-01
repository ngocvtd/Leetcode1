class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result = [''] * len(s) 
        for i in range(len(s)):
            result[indices[i]] = s[i] 
        return ''.join(result) 
