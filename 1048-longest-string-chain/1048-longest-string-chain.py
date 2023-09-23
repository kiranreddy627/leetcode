class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d=defaultdict(int)
        for w in sorted(words,key=len):
            n,d[w]=len(w),1
            for i in range(n):
                wo=w[:i]+w[i+1:]
                if wo in d:
                    d[w]=max(d[w],d[wo]+1)
        return max(d.values())