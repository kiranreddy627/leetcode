class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph=defaultdict(list)
        n=len(points)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    graph[i].append((abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1]),j))
        heap=[(0,0)]
        res=0
        vis=set()
        while heap:
            a,b=heapq.heappop(heap)
            if b in vis:
                continue
            res+=a
            vis.add(b)
            for x,y in graph[b]:
                if y not in vis:
                    heapq.heappush(heap,(x,y))
        return res