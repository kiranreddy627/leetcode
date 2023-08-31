class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        d=defaultdict(list)
        for i in range(n+1):
            d[i]=[i-ranges[i],i+ranges[i]]
        res=[0,n]
        lst=list(d.values())
        lst.sort()
        lst.append([10**9,10**9])
        start=res[0]
        end=res[0]-1
        i=0
        cnt=0
        while i<len(lst):
            if lst[i][0]<=start:
                end=max(lst[i][1],end)
                i+=1
            else:
                start=end
                cnt+=1
                if lst[i][0]>end or end>=res[1]:
                    break
        if end<res[1]:return -1
        return cnt