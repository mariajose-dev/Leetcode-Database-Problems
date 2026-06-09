class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis=[]
        for x in s:
            if x in "1234567890":
                if int(x) in lis:
                    continue
                else:
                    lis.append(int(x))
        lis.sort()
        if len(lis)>1:
            return lis[-2] 
        else:
            return -1