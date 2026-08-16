class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis=[]
        co=0
        for x in nums:
            if x==0:
                lis.append(co)
                co=0
            if x==1:
                co+=1
        lis.append(co)
        return max(lis)