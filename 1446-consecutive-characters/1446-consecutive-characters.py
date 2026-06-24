class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        ans = 1

        for i in range(1, len(s)):

            if s[i] == s[i-1]:

                count += 1

            else:

                count = 1

            ans = max(ans, count)

        return ans
