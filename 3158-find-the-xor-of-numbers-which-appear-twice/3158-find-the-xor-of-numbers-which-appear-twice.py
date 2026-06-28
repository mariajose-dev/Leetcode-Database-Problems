class Solution(object):
    def duplicateNumbersXOR(self, nums):
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
            if dic[x]==2:
                lis.append(x)
        if len(lis)<1:
            return 0
        if len(lis)==1:
            return lis[0]
        if len(lis)>1:
            res=lis[0]
            for i in range(len(lis)):
                if i==0:
                    continue
                res^=lis[i]
            return res


