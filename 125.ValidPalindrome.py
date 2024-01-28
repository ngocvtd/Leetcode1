class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rs = ""
        for c in s:
            if c.isalnum():
                rs += c

        str_palin = rs.lower()

        return str_palin == str_palin[::-1]
        
        
    
    
        
