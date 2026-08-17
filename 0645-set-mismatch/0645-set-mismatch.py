class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1=set(nums)
        n=len(nums)
        Natural_sum=n*(n+1)//2
        sum_set1=sum(set1)
        actual_sum=sum(nums)

        duplicate = actual_sum - sum_set1
        missing = Natural_sum - sum_set1
        
        return [duplicate, missing]




        