class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        else:
            res=sum(list(int(i) for i in str(num)))
            if len(str(res))>1:
                return self.addDigits(res)
            else:
                return res