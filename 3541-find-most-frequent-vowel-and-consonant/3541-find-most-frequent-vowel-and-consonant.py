class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic1 = {}

        for st in s:

            if st in dic1:
                dic1[st] += 1

            else:
                dic1[st] = 1

        max_vowel = 0
        max_consonant = 0

        for x in dic1:

            if x in "aeiou":

                max_vowel = max(max_vowel, dic1[x])

            else:

                max_consonant = max(max_consonant, dic1[x])

        return max_vowel + max_consonant
