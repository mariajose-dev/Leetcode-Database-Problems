class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup=0
        x=[]
        for i in nums:
            if i in x:
                dup=dup^i
            x.append(i)
        return dup

