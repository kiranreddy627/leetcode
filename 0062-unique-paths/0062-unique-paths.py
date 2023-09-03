class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[0 for j in range(m)]for i in range(n)]
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for j in range(m+1)] for i in range(n+1)]
        def dps(i,j,grid):
            if i==n-1 and j==m-1:
                return 1
            w1=0
            w2=0
            if dp[i][j]!=-1:
                return dp[i][j]
            if i+1<n and grid[i+1][j]==0:
                w1=dps(i+1,j,grid)
            if j+1<m and grid[i][j+1]==0:
                w2=dps(i,j+1,grid)
            ans=w1+w2
            dp[i][j]=ans
            return ans
        if grid[0][0]==1:
            return 0
        return dps(0,0,grid)