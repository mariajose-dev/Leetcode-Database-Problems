class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        co = 0
        temp = word

        while temp in sequence:
            co += 1
            temp += word

        return co