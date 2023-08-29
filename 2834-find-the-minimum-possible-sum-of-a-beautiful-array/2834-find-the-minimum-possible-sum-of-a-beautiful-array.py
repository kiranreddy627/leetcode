class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        lst=set()
        i=1
        res=0
        while n>0:
            if (target-i) not in lst:
                res+=i
                lst.add(i)
                n-=1
            i+=1
        return res