class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openChars = ['(', '[', '{']
        closeChars = [')', ']', '}']

        for c in s :
            if c in openChars:
                stack.append(c)
            elif c in closeChars:
                if not stack or stack.pop() != openChars[closeChars.index(c)]:
                    return False

        return not stack
