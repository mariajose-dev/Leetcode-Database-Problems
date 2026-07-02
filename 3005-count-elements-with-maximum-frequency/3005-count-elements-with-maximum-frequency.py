class Solution(object):
    def maxFrequencyElements(self, nums):
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
        val=list(dic.values())
        m=max(val) 
        ans=0
        for x in dic:
            if dic[x]==m:
                ans+=dic[x]
        return ans 