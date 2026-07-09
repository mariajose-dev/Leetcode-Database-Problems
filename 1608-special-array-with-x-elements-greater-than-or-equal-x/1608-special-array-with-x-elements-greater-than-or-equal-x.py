class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(len(nums)+1):
            co=0
            for i in nums:
                if i>=x:
                    co+=1
            if co==x:
                return x
        return -1