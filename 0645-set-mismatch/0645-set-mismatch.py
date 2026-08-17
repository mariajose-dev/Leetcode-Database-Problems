class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        dic={}
        ans=[]
        for x in nums:
            if x not in dic:
                dic[x]=1
            else:
                ans.append(x)
        
        num_set=set(nums)

        for x in range(1,n+1):
            if x not in nums:
                ans.append(x)
        return ans

        