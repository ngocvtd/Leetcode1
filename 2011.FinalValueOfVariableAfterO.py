class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        rs = 0
        for c in operations:
            if c == '--X' or c == 'X--':
                rs -=1
            else:
                rs +=1
        return rs
            
