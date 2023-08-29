class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i=0
        while i<=len(s):
            res=""
            if i+len(part)<=len(s) and s[i:i+len(part)]==part:
                res=s[:i]+s[i+len(part):]
                i=0
                s=res
            else:
                i+=1
        return s