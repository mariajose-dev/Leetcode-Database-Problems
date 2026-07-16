class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum_ans=0
        for x in accounts:
            row_sum=0
            for i in range (len(x)):
                row_sum+=x[i]
            sum_ans=max(sum_ans,row_sum)
        return sum_ans