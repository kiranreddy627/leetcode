class Solution:
    def groupThePeople(self, grp: List[int]) -> List[List[int]]:
        res=[]
        d=defaultdict(list)
        for i in range(len(grp)):
            d[grp[i]].append(i)
        for x,y in d.items():
            if len(y)<=x:
                res.append(y)
            else:
                i=0
                while (i+x)<len(y):
                    res.append(y[i:i+x])
                    i=i+x
                else:
                    res.append(y[i:])
        return res