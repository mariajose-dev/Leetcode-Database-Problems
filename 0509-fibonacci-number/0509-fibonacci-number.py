class Solution(object):
    def fib(self, n):
        dp=[0]
        if n==0:
            return dp[0]
        dp.append(1)

        if n==1:
            return dp[1]
        
        for i in range(2,n+1):
            dp.append(dp[-1]+dp[-2])
        
        return dp[-1]


        
        