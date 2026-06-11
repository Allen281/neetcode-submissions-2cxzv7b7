class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()

        def solve(i:int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = solve(i+1, buying)
            if buying:
                buy = solve(i+1, False) - prices[i]
                dp[(i, True)] = max(buy, cooldown)
            else:
                sell = solve(i+2, True) + prices[i]
                dp[(i, False)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return solve(0, True)
            

