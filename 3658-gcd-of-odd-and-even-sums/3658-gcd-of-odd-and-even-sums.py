class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumOdd = n * n
        sumEven = n * (n + 1)

        gcd = 1

        for i in range(1, sumOdd/2+1):
            if sumOdd % i == 0 and sumEven % i == 0:
                gcd = i

        return gcd