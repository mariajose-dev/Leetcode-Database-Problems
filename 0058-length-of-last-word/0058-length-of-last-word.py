class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split()
        print(words)
        w=words[-1]
        return len(w)