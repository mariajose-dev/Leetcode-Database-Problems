class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}

        for x in nums:

            if x in dic:
                dic[x] += 1

            else:
                dic[x] = 1

        set1 = set()

        for x in nums:

            if dic[x] == 2:
                set1.add(x)

        return list(set1)