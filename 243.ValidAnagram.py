class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False

        arr_s = list(s)
        arr_t = list(t)

        arr_s.sort()
        arr_t.sort()

        return arr_s == arr_t
