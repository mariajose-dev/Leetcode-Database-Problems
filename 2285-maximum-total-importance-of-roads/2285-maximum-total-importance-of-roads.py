class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        res=0
        cost=1 #start from 1 to n
        conn=[0]*n
        #to calculate all the connections from each node
        for road in roads:
            conn[road[0]]+=1
            conn[road[1]]+=1
        conn.sort()
        for c in conn:
            res+=c*cost
            cost+=1
        return res