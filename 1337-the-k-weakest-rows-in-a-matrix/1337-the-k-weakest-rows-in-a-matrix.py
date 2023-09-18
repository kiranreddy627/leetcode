class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res=[]
        for i in range(0,len(mat)):
            res.append([i,mat[i].count(1)])
        res.sort(key=lambda x:x[1])
        ans=[]
        for i in range(k):
            ans.append(res[i][0])
        return ans