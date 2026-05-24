class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic={}
        for x in arr:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
            
        print(dic)

        lis=[]

        for x in dic:
            if dic[x]==x:
                lis.append(x)
        
        if lis:
            return max(lis)
        else:
            return -1