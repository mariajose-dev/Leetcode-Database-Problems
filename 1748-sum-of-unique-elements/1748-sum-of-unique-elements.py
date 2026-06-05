class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        sum=0
        for x in dic:
            if dic[x]==1:
                sum+=x
        return sum