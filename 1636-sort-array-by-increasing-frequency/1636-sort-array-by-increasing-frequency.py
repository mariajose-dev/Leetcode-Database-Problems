class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis=[]
        dic={}
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1

        for k in sorted(dic,key=lambda x: (dic[x], -x)):
            for i in range(dic[k]):
                lis.append(k)
                
        return lis