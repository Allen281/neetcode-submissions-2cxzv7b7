class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colPlaced = set()
        posDiag = set()
        negDiag = set()

        rslt = list()
        board = [['.' for _ in range(n)] for _ in range(n)]

        def solve(r: int) -> None:
            if r == n:
                formatted_board = ["".join(row) for row in board]
                rslt.append(formatted_board.copy())
                return
        
            
                
            for c in range(n):
                if c in colPlaced or r+c in posDiag or r-c in negDiag:
                    continue
                    
                board[r][c] = 'Q'
                colPlaced.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                solve(r+1)

                colPlaced.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'
        
        solve(0)
        return rslt