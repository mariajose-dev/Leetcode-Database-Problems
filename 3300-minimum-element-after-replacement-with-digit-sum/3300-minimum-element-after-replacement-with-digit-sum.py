class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis=[]
        for x in nums:
            s=0
            while x!=0:
                r=x%10
                x=x//10
                s+=r
            lis.append(s)
        print(lis)
        lis.sort()
        print(lis)
        return lis[0]