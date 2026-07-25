class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=str(n)
        prod=0
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                prod=max(prod,int(num[i])*int(num[j]))
        return prod
        