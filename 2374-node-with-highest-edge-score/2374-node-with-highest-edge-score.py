class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        d=defaultdict(int)
        for i in range(len(edges)):
            d[edges[i]]+=i
        res=max(list(d.values()))
        mini=10**9
        for i in d.keys():
            if d[i]==res:
                mini=min(mini,i)
        return mini