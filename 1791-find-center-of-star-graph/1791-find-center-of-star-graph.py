class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        dic={}
        for x,y in edges:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
            
            if y in dic:
                dic[y]+=1
            else:
                dic[y]=1
        
        mx = 0
        ans = 0

        for item in dic:

            if dic[item] > mx:
                mx = dic[item]
                ans = item

        return ans