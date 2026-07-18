class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for x in nums:
            dic[x] = 1
        ans = -1
        for x in dic:
            if x > 0 and -x in dic:
                ans = max(ans, x)
        return ans
