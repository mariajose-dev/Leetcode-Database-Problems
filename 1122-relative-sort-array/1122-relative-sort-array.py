class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lis=[]
        dic1={}
        for x in arr1:
            if x in dic1:
                dic1[x]+=1
            else:
                dic1[x]=1
        
        for x in arr2:
            if x in dic1:
                for i in range(0,dic1[x]):
                    lis.append(x)

        arr1.sort()
        for x in arr1:
            if x not in arr2:
                lis.append(x)
        return lis
        