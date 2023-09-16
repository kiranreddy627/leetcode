class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r=len(heights)
        c=len(heights[0])
        dire=[(0,1),(0,-1),(1,0),(-1,0)]
        dist=[[10**9 for _ in range(c)] for _ in range(r)]
        dist[0][0]=0
        heap=[(0,0,0)] 
        while heap:
            e,x,y=heappop(heap)
            if x==r-1 and y==c-1:
                return e
            for dx,dy in dire:
                nx,ny=x+dx,y+dy
                if 0<=nx<r and 0<=ny<c:
                    new=max(e,abs(heights[x][y]-heights[nx][ny]))
                    if new<dist[nx][ny]:
                        dist[nx][ny]=new
                        heappush(heap, (new, nx, ny))