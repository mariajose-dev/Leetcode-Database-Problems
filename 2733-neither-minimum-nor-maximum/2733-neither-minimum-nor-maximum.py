class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lim=len(nums)
        if (lim<=2):
            return -1
        else:
            nums.sort()
            return nums[1]
