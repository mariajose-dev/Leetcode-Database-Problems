class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st=""
        for i in digits:
            st+=str(i)

        #print(st)

        stnum=int(st)
        #print(stnum)
        stnum=stnum+1
        lis=[]
        while stnum!=0:
            r=stnum%10
            stnum=stnum//10
            lis.append(r)
        return lis[::-1]