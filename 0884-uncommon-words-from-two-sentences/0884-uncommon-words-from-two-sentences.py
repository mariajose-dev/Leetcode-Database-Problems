class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        lis=[]
        dic={}
        l1=s1.split()
        l2=s2.split()
        for x in l1:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        
        for y in l2:
            if y in dic:
                dic[y]+=1
            else:
                dic[y]=1
        
        for x in dic:
            if dic[x]==1:
                lis.append(x)
        return lis