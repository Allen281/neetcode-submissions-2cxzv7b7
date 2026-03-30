class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)

        def solve(amt):
            if amt < 0:
                return -1
            
            if amt == 0:
                return 0
            
            if dp[amt] != -1:
                return dp[amt]

            for i in coins:
                temp = solve(amt-i)+1
                if temp != 0 and temp != -1:
                    dp[amt] = temp if dp[amt] == -1 else min(dp[amt], temp)

            if dp[amt] == -1:
                dp[amt] = -2
                return -1

            return dp[amt]

        return solve(amount)