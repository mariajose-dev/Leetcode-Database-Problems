class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for x in nums:
            if x not in dic:
                dic[x]=1
            else:
                dic[x]+=1
        maxFreq = 0
        ans = -1

        for x in sorted(dic):
            if x % 2 == 0:
                if dic[x] > maxFreq:
                    maxFreq = dic[x]
                    ans = x

        return ans