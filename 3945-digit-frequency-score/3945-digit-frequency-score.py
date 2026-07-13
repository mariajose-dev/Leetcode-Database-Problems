class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        dic={}
        lis=list(map(int,str(n)))
        for x in lis:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        
        for k,v in dic.items():
            ans+=k*v
        return ans