class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumodd=0
        sumeven=0
        for i in range(1,n+1):
            if i%2==0:
                sumeven+=i
            else:
                sumodd+=i
        lis=[]
        lim=max(sumodd,sumeven)
        for x in range(1,lim+1):
            if sumodd%x==0 and sumeven%x==0:
                lis.append(i)
        return max(lis)