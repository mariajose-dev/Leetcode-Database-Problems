class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={}
        for x in s:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        lis=dic.values()
        num=lis[0]
        for x in lis:
            if x!=num:
                return False
        return True