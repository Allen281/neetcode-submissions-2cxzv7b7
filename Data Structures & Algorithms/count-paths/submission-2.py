class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        for x in range(m):
            for y in range(n):
                if x != 0:
                    dp[x][y] += dp[x-1][y]
                if y != 0:
                    dp[x][y] += dp[x][y-1]
        
        return dp[m-1][n-1]
