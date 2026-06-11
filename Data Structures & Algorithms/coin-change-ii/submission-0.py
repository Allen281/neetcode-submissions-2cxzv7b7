class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = dict()

        def solve(i: int, goal: int) -> int:
            if goal == 0:
                return 1
            if i < 0 or goal < 0:
                return 0
            if (i, goal) in dp:
                return dp[(i, goal)]
            
            ways = solve(i-1, goal)

            if goal >= coins[i]:
                ways += solve(i, goal-coins[i])
            
            dp[(i, goal)] = ways
            return ways
        
        return solve(len(coins)-1, amount)
