class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans_lis=[]
        big=max(candies)
        for x in candies:
            if x+extraCandies>=big:
                ans_lis.append(True)
            else:
                ans_lis.append(False)
        return ans_lis