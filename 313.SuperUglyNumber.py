class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1

        ugly = [0] * n
        ugly[0] = 1
        idx = [0] * len(primes)

        for i in range(1, n):
            temp = float('inf')
            for j in range(len(primes)):
                temp = min(temp, primes[j] * ugly[idx[j]])

            ugly[i] = temp

            for j in range(len(primes)):
                if temp == primes[j] * ugly[idx[j]]:
                   idx[j] += 1

        return ugly[-1]
