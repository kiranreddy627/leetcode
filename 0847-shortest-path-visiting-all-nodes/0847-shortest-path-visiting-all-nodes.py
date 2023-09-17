class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        q=deque([(1<<i,i,0) for i in range(n)])
        vis=set((1<<i,i) for i in range(n))
        while q:
            mask,node,dist=q.popleft()
            if mask==(1<<n)-1:
                return dist
            for k in graph[node]:
                new=mask | (1<<k)
                if (new,k) not in vis:
                    vis.add((new,k))
                    q.append((new,k,dist+1))
