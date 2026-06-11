class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        dic={}
        for i in range(len(names)):
            dic[heights[i]]=names[i]
        lis=[]
        for x in sorted(dic,reverse=True):
            lis.append(dic[x])
        return lis