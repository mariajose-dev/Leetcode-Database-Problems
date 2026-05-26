class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        low = set()
        up = set()

        for ch in word:

            if ch.islower():
                low.add(ch)

            else:
                up.add(ch.lower())

        co = 0

        for x in low:

            if x in up:
                co += 1

        return co