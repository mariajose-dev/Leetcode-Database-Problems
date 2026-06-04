class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=0
        for x in nums:
            co=0
            while x!=0:
                x=x//10
                co+=1
            if co%2==0:
                num+=1
        return num