class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        co = 0
        pos = 0

        for x in s:
            if x in t[pos:]:
                co += 1
                pos = t.index(x, pos) + 1
        if co==len(s):
            return True
        else:
            return False