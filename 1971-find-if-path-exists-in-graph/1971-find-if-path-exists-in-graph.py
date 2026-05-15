class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        neighbors=defaultdict(list)
        for n1,n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        q=deque([source]) #double ended queue created by default
        seen=set([source])

        while q:
            node=q.popleft()
            if node==destination:
                return True
            
            for n in neighbors[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        return False