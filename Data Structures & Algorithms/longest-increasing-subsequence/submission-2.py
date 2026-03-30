class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        rslt = 1
        for i in range(1, len(nums)):
            maxLen = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxLen = max(maxLen, dp[j]+1)
            
            dp[i] = maxLen
            rslt = max(rslt, maxLen)
        

        return rslt