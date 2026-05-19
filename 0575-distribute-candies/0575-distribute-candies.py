class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        notypes=len(set(candyType))

        tot_candies=len(candyType)//2

        if tot_candies<=notypes:
            return tot_candies
        else:
            return notypes
