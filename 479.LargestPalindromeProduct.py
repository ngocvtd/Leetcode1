class Solution(object):

    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rv = str(x)[::-1]
        num_rv = int(rv)
        return num_rv == x

    def largestPalindrome(self, n):
        if n == 1:
            return 9
        left_limit = 10 ** (n - 1)
        right_limit = 10 ** n - 1
        max_palindrome = 0
        for i in range(right_limit, left_limit - 1, -1):
            for j in range(i, left_limit - 1, -1):
                rs = i * j
                if rs <= max_palindrome:
                    break
                if self.isPalindrome(rs):
                    max_palindrome = rs
        return max_palindrome % 1337
