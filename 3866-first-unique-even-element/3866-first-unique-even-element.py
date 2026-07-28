class Solution(object):
    def firstUniqueEven(self, nums):
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

        lis=[]
        for x in dic:
            if dic[x]==1 and x%2==0:
                lis.append(x)
        if lis:
            pos = len(nums)
            for x in lis:
                pos = min(nums.index(x), pos)
            return nums[pos]    
        else:
            return -1