class Solution:
    def minExtraChar(self, s: str, dict: List[str]) -> int:
        res=len(s)
        dp=[0]*(res+1)
        vis=set(dict)
        for i in range(1,len(s)+1):
            dp[i]=dp[i-1]+1
            for j in range(i):
                if s[j:i] in vis:
                    dp[i]=min(dp[i],dp[j])
        return dp[res]