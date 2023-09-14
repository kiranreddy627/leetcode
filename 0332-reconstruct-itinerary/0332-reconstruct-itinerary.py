class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d=defaultdict(list)
        for a,b in tickets:
            if a in d:
                d[a].append(b)
            else:
                d[a]=[b]
        for i in d.keys():
            d[i].sort(reverse=True)
        stack=[]
        res=[]
        stack.append("JFK")
        while len(stack)>0:
            k=stack[-1]
            if k in d and len(d[k])>0:
                stack.append(d[k].pop())
            else:
                res.append(stack.pop())
        return res[::-1]