class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()      # columns where queens are placed
        pos_diag = set()  # (r+c) → positive diagonal
        neg_diag = set()  # (r-c) → negative diagonal

        def backtrack(r):
            if r == n:
                # Found a valid placement, save solution
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue  # not safe
                
                # place queen
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)

                # move to next row
                backtrack(r+1)

                # undo (backtrack)
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)

        backtrack(0)
        return res
