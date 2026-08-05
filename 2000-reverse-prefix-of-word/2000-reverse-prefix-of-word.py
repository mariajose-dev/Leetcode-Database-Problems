class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        else:
            ind=word.index(ch)
            st=word[:ind+1]
            return st[::-1]+word[ind+1:]

        