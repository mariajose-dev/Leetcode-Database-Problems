class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        st1=""
        st2=""
        for x in word1:
            st1+=x
        for y in word2:
            st2+=y
        if st1==st2:
            return True
        else:
            return False