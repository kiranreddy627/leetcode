class Solution:
    def eraseOverlapIntervals(self, vals: List[List[int]]) -> int:
        vals.sort(key=lambda x:x[1])
        # print(vals)
        end=-10**9
        res=0
        for a,b in vals:
            if a>=end:end=b
            else:res+=1
        return res