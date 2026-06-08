class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis=[]
        for x in nums:
            co=0
            for y in nums:
                if x>y:
                    co+=1
            lis.append(co)
        return lis
            