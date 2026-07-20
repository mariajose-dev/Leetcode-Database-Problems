class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st=list(s.split())
        ans=""
        for i in range(0,k):
            ans+=st[i]
            ans+=" "
        return ans[:-1]