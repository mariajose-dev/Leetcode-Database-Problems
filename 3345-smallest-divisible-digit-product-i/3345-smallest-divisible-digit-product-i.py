class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        temp=n
        while temp>=n:
            num=temp
            prod=1
            while num!=0:
                r=num%10
                prod*=r
                num=num//10
            if prod%t==0:
                return temp
            else:
                temp+=1
            
            
            
        