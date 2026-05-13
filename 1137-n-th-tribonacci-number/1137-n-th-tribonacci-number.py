class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]

        if n==0:
            return dp[0] 

        dp.append(1)

        if n==1:
            return dp[1]
        
        dp.append(1)

        if n==2:
            return dp[2]

        for i in range(3,n+1):
            dp.append(dp[-1]+dp[-2]+dp[-3])
        return dp[-1]