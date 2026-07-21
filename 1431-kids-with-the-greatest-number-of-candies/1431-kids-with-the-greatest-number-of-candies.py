class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans_lis=[]
        for x in candies:
            if x+extraCandies>=max(candies):
                ans_lis.append(True)
            else:
                ans_lis.append(False)
        return ans_lis