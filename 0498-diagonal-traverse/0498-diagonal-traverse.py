class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        res=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])
        for i in range(len(d.keys())):
            if i%2==0:
                res.extend([i for i in d[i][::-1]])
            else:
                res.extend([i for i in d[i]])
        return res