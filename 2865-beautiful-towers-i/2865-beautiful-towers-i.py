class Solution:
    def maximumSumOfHeights(self, m: List[int]) -> int:
        ma=-10**9 
        for ind in range(len(m)):
            res=[]
            res.append(m[ind])
            maxi=m[ind]
            for i in range(ind-1,-1,-1):
                if m[i]<=maxi:
                    maxi=m[i]
                    res.insert(0,maxi)
                else:
                    res.insert(0,maxi)
            maxi=m[ind]
            for i in range(ind+1,len(m)):
                if m[i]<=maxi:
                    maxi=m[i]
                res.append(maxi)
            ma=max(ma,sum(res))
        return ma