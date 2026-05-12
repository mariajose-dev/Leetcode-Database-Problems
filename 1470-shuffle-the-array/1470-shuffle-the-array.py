class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        lis=[]
        i=0
        j=n
        while i<n and j<2*n:
            lis.append(nums[i])
            i=i+1
            lis.append(nums[j])
            j=j+1

        return lis