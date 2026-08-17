class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        co = 0

        for i in range(len(s)):

            zero = 0
            one = 0

            for j in range(i, len(s)):

                if s[j] == "0":
                    zero += 1
                else:
                    one += 1

                if zero <= k or one <= k:
                    co += 1

        return co