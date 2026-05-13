class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        
        dp=[0]*len(cost)

        dp[0]=cost[0] #first value in cost array stored in dp array

        if len(cost)>=2:
            dp[1]=cost[1] #store second value in dp array if len(cost) grt than 2 

        for i in range (2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])

        return min(dp[-1],dp[-2])