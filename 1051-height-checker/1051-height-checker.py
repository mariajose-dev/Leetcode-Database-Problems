class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        exp=[]
        for x in heights:
            exp.append(x)
        heights.sort()
        co=0
        for i in range(len(heights)):
            if exp[i]!=heights[i]:
                co+=1
        return co