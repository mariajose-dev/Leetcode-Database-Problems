class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        m=0
        for i in range(l):
            for j in range(i+1,l):
                m=max(m,(nums[i]-1)*(nums[j]-1))
        return m