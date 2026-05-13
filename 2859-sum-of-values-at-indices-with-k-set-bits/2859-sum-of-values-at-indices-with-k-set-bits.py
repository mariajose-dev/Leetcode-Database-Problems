class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=[0]*(len(nums))

        for i in range(0,len(nums)):
            ans[i]=ans[i>>1]+(i&1)
        print(ans)
        sum=0
        for i in range(len(ans)):
            if ans[i]==k:
                sum+=nums[i]
        print(sum)
        return sum