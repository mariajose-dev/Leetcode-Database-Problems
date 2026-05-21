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
                dic[x]+=1
        
        num_set=set(nums)

        for i in dic:
            if dic[i]>1:
                ans.append(i)

        for x in range(1,n+1):
            if x not in nums:
                ans.append(x)
        return ans

        