class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        r = x // 2

        while r * r > x:
            r = (r + x // r) // 2

        return r