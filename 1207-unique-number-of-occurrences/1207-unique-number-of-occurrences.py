class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic={}
        for x in arr:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        
        s=set(arr)
        lis=[]
        for x in s:
            lis.append(dic[x])

        print(lis)

        ans_dic={}
        for k in lis:
            if k in ans_dic:
                ans_dic[k]+=1
            else:
                ans_dic[k]=1

        for x in ans_dic:
            if ans_dic[x]>1:
                return False
        return True   
