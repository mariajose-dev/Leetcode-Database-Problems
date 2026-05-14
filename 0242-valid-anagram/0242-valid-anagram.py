class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        for i in range (len(s)):
            if s[i] not in t:
                return False
        '''
        if sorted(s)==sorted(t):
            return True
        else:
            return False