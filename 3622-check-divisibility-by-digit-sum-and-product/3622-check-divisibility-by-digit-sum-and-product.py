class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=n
        sum_num=0
        prod_num=1
        while num!=0:
            r=num%10
            num=num//10
            sum_num+=r
            prod_num*=r
        if n%(prod_num+sum_num)==0:
            return True
        else:
            return False