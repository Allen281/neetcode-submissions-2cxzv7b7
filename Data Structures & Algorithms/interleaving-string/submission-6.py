class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if len(s3) != m+n:
            return False
        
        dp = [False] * (n+1)
        dp[n] = True

        for j in range(n-1, -1, -1):
            dp[j] = dp[j+1] and s2[j] == s3[m+j]

        for i in range(m-1, -1, -1):
            dp[n] = dp[n] and s1[i] == s3[n+i]
            for j in range(n-1, -1, -1):
                take1 = dp[j] and s1[i] == s3[i+j]
                take2 = dp[j+1] and s2[j] == s3[i+j]

                dp[j] = take1 or take2
        
        return dp[0]