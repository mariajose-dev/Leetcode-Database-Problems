class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        st=set(nums)

        lis=[]
        for x in range(1,n+1):
            if x not in st:
                lis.append(x)
        return lis