class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        lis = []

        for i in range(1, n+1):
            lis.append(i)

        if n == 1:
            return 1

        for x, y in trust:

            if x in lis:
                lis.remove(x)

        # no candidate
        if len(lis) == 0:
            return -1

        judge = lis[0]

        count = 0

        for x, y in trust:

            if y == judge:
                count += 1

            if count == n - 1:
                return judge

        return -1