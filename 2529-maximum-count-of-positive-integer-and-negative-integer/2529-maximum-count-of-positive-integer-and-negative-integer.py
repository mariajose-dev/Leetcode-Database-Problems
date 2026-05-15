class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        posco=0
        negco=0
        for x in nums:
            if x<0:
                negco+=1
            elif x>0:
                posco+=1
            elif x==0:
                continue
        return max(posco,negco)