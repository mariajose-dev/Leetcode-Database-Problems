class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        indegree = [0] * (n + 1) #who voted
        outdegree = [0] * (n + 1) #who got vote

        for x in trust:

            outdegree[x[0]] += 1
            indegree[x[1]] += 1

        for i in range(1, n + 1):

            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i

        return -1