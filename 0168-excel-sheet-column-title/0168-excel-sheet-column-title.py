class Solution:
    def convertToTitle(self, n: int) -> str:
        def func(n):
            if n==0:
                return ""
            else:
                r=(n-1)%26
                res=chr(ord("A")+r)
            return func((n-1)//26)+res
        return func(n)