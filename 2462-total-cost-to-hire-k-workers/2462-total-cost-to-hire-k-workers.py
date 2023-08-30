import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res=0
        a,b=[],[]
        heapq.heapify(a)
        heapq.heapify(b)
        i,j=0,len(costs)-1
        for _ in range(k):
            while len(a)<candidates and i<=j:
                heappush(a,costs[i])
                i+=1
            while len(b)<candidates and j>=i:
                heappush(b,costs[j])
                j-=1
            if len(a)==0: heappush(a,10**9)
            if len(b)==0: heappush(b,10**9)
            x=heappop(a)
            y=heappop(b)
            mini=min(x,y)
            res+=mini
            if mini==x: heappush(b,y)
            else: heappush(a,x)
        return res