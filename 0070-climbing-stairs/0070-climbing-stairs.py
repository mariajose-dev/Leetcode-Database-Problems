class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pn=0
        nn=0
        cn=1
        co=0

        if n==1:
            return 1
        
        while co<n:
            nn=pn+cn
            pn=cn
            cn=nn
            co=co+1
        return nn
        