class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        print(dic)
        lis=[]
        co=0
        for i in sorted(dic, key=dic.get, reverse=True):
            if co<k:
                co+=1
                lis.append(i)

        return lis