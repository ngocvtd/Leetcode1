class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_count = 0
        
        for sentence in sentences:
            words = sentence.split()
            word_count = len(words)
            max_count = max(max_count, word_count)
        
        return max_count
