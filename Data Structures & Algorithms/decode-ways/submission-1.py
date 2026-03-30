class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)

        def solve(i):
            if(i >= len(s)):
                return 1
            
            if s[i] == '0':
                dp[i] = 0

            if dp[i] != -1:
                return dp[i]
            
            dp[i] = solve(i+1)
            
            if i+1 < len(s):
                if s[i] == '1':
                    dp[i] += solve(i+2)
                elif s[i] == '2' and s[i+1] <= '6':
                    dp[i] += solve(i+2)
            
            return dp[i]
        
        return solve(0)