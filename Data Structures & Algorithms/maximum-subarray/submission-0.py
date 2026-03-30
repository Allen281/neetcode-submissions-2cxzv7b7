class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minSum = 0
        curSum = 0
        rslt = -1e9

        for n in nums:
            curSum += n
            rslt = max(rslt, curSum-minSum)
            minSum = min(minSum, curSum)
        
        return rslt