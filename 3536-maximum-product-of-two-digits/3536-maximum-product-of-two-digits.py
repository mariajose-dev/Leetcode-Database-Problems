class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=str(n)
        prod=0
        l=len(num)
        for i in range(l):
            for j in range(i+1,l):
                prod=max(prod,int(num[i])*int(num[j]))
        return prod
        