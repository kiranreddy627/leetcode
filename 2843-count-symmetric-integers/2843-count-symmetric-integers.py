class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low,high+1):
            n=len(str(i))
            s=str(i)
            if n%2==0:
                n=n//2
                if sum(map(int,list(s[:n])))==sum(map(int,list(s[n:]))):
                    res+=1
        return res