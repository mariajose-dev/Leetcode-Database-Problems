class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=[]
        for x in s:
            if x.isdigit():
                if int(x) not in lis:
                    lis.append(int(x))
        lis.sort()
        if len(lis)< 2:
            return -1
        
        return lis[-2]