class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis=[]
        for x in nums:
            lis.append(x*x)
        lis.sort()
        return lis