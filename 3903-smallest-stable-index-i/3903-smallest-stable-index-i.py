class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            maxx=max(nums[0:i+1])
            minn=min(nums[i:])
            val=maxx-minn
            if val<=k:
                return i
        return -1