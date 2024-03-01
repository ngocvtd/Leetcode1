class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        rs = []
        for i in range(len(words)):
            for c in words[i]:
                if c == x:
                    rs.append(i)
                    break
        return rs
