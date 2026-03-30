class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowsToClear, colsToClear = set(), set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rowsToClear.add(r)
                    colsToClear.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in rowsToClear or c in colsToClear:
                    matrix[r][c] = 0
        