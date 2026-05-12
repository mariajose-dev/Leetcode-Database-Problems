class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lis=[]
        if n==1:
            return True
        lis.append(n)
        for item in lis:
            sqr=0
            while item!=0:
                r=item%10
                item=item//10
                sqr+=r*r
            if sqr in lis:
                return False
            lis.append(sqr)
            if 1 in lis:
                return True
