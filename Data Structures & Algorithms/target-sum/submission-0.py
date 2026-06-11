class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = dict()

        def solve(i: int, curVal: int) -> int:
            if i < 0:
                return 1 if curVal == 0 else 0
            if (i, curVal) in dp:
                return dp[(i, curVal)]
            
            ways = solve(i-1, curVal-nums[i]) + solve(i-1, curVal+nums[i])
            dp[(i, curVal)] = ways
            return ways
        
        return solve(len(nums)-1, target)