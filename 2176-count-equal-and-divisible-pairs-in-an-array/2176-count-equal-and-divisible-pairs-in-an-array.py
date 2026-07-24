class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        co=0
        length=len(nums)
        for i in range(0,length):
            for j in range(i+1,length):
                if nums[i]==nums[j] and (i*j)%k==0:
                    co+=1
        return co