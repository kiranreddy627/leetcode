class Solution:
    def minDeletions(self, s: str) -> int:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        lst=list(d.values())
        vis=set()
        res=0
        for i in lst:
            while i>0 and i in vis:
                i-=1
                res+=1
            vis.add(i)
        return res