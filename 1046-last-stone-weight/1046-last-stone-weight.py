class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:

            stones.sort()

            fh = stones[-1]   # biggest
            sh = stones[-2]   # second biggest

            stones.pop()
            stones.pop()

            if fh - sh != 0:
                stones.append(fh - sh)

        if stones:
            return stones[0]

        return 0
         
