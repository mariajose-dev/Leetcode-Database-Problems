class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic1={}
        s=set()
        for x in nums:
            if x in dic1:
                dic1[x]+=1
                s.add(x)
            else:
                dic1[x]=1

        return list(s)