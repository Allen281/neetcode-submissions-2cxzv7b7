class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        max_values = [[-1] * n for _ in range(m)]

        def solve(x, y, prev) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= prev:
                return 0
            if max_values[x][y] != -1:
                return max_values[x][y]

            cur = matrix[x][y]
            max_values[x][y] = 1 + max(solve(x+1, y, cur), 
                                        solve(x-1, y, cur),
                                        solve(x, y+1, cur),
                                        solve(x, y-1, cur))
            return max_values[x][y]

        rslt = 0
        for i in range(m):
            for j in range(n):
                rslt = max(rslt, solve(i, j, -1))
        return rslt


