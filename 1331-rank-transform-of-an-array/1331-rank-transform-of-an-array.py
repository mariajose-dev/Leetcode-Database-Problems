class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ar1 = arr[:]
        arr.sort()
        dic = {}
        rank = 1
        for x in arr:
            if x not in dic:
                dic[x] = rank
                rank += 1
        lis = []
        for x in ar1:
            lis.append(dic[x])
        return lis