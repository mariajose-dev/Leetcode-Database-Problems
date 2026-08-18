class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n=len(nums)
        res=0
        i=0
        while i<n:
            if nums[i]%2==0 and nums[i]<=threshold:
                start=i
                i+=1
                while i<n and nums[i] <=threshold and nums[i]%2!=nums[i-1]%2:
                    i+=1
                res=max(res,i-start)
            else:
                i+=1
        return res