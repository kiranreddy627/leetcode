class Solution:
    def totalNQueens(self, n: int) -> int:
        board=[["0"]*n for i in range(n)]
        col=set()
        pos=set()
        neg=set()
        res=0
        def backtrack(r):
            nonlocal res
            if r==n:
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c]="1"
                backtrack(r+1)
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c]="0"
        backtrack(0)
        return res