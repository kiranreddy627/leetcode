class Solution:
    def strangePrinter(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        def rec(i,j,s):
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=10**9
            for k in range(i,j):
                mini=min(mini,rec(i,k,s)+rec(k+1,j,s))
            dp[i][j]=mini-int(s[i]==s[j])
            return dp[i][j]
        return rec(0,n-1,s)