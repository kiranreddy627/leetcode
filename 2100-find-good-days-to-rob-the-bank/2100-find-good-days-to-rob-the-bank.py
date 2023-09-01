class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        suf=[0]*len(security)
        for i in range(len(security)-2,0,-1):
            if security[i]<=security[i+1]:
                suf[i]=suf[i+1]+1
        res=[]
        pre=0
        for i in range(len(security)-time):
            if i and security[i-1]>=security[i]:
                pre+=1
            else:
                pre=0
            if pre>=time and suf[i]>=time:
                res.append(i)
        return res
