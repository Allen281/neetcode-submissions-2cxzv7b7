class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = totalSum // 2

        dp = [False] * (target+1)
        dp[0] = True

        for s in stones:
            for i in range(target, s-1, -1):
                dp[i] |= dp[i-s]

        for i in range(target, -1, -1):
            if dp[i]:
                return totalSum - (2*i)