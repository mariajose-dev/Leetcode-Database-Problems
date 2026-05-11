class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        parts = []
        count = 0
        start = 0

        # split into primitive parts
        for i in range(len(s)):

            if s[i] == '(':
                count += 1
            else:
                count -= 1

            # primitive completed
            if count == 0:
                parts.append(s[start:i+1])
                start = i + 1

        # remove outer parentheses
        res = ""

        for part in parts:
            res += part[1:-1]

        return res
        