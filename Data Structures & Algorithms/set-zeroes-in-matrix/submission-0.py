class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToClear, colsToClear = set(), set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rowsToClear.add(r)
                    colsToClear.add(c)

        for r in range(len(matrix)):
            if r in rowsToClear:
                for c in range(len(matrix[r])):
                    matrix[r][c] = 0
        
        for c in range(len(matrix[0])):
            if c in colsToClear:
                for r in range(len(matrix)):
                    matrix[r][c] = 0
        