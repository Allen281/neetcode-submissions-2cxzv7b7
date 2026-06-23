class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        placed = list()
        rslt = list()

        def solve(board: list, col1: int, count: int) -> None:
            if count == n and col1 == n:
                formatted_board = ["".join(row) for row in board]
                rslt.append(formatted_board.copy())
                return
            
            for row1 in range(n):
                good = True
                for row2, col2 in placed:
                    slope = abs((row2-row1)/(col2-col1))

                    if slope == 0 or slope == 1:
                        good = False
                        break
                
                if not good:
                    continue
                    
                board[row1][col1] = 'Q'
                placed.append((row1, col1))
                solve(board, col1+1, count+1)
                placed.pop()
                board[row1][col1] = '.'
        
        temp = [['.' for _ in range(n)] for _ in range(n)]
        solve(temp, 0, 0)
    
        return rslt