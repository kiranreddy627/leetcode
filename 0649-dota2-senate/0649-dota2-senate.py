class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        lr=[]
        ld=[]
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                lr.append(i)
            else:
                ld.append(i)
        while lr and ld:
            r,d=lr.pop(0),ld.pop(0)
            if r<d:
                lr.append(r+n)
            else:
                ld.append(d+n)
        if len(lr)>len(ld):
            return "Radiant"
        return "Dire"