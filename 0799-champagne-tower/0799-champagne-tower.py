class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev=[[0.0]*i for i in range(1,101)]
        prev[0][0]=poured
        for row in range(query_row):
            for i in range(row+1):
                ex=(prev[row][i]-1.0)
                if ex>0:
                    prev[row+1][i]+=0.5*ex
                    prev[row+1][i+1]+=0.5*ex
        return min(1.0,prev[query_row][query_glass])