class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        l1=list(s1)
        l2=list(s2)
        if sorted(l1[::2])==sorted(l2[::2]) and sorted(l1[1::2])==sorted(l2[1::2]):
            return True
        return False