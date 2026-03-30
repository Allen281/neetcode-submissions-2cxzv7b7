class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rslt = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp_max = curMax 
            
            curMax = max(n, temp_max * n, curMin * n)
            curMin = min(n, temp_max * n, curMin * n)
            
            rslt = max(rslt, curMax)

        return rslt