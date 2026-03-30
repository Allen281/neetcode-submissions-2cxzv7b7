class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(nums: List[int], values: List[int], i, end) -> int:
            if i > end:
                return 0

            if values[i] != -1:
                return values[i]

            values[i] = 0
            plus1 = solve(nums, values, i+1, end)
            plus2 = solve(nums, values, i+2, end) + nums[i]

            values[i] = max(plus1, plus2)
            return values[i]

        start_list = [-1]*len(nums)
        rslt = max(solve(nums, start_list, 0, len(nums)-2), nums[0])
        start_list = [-1]*len(nums)
        rslt = max(rslt, solve(nums, start_list, 1, len(nums)-1))
        
        return rslt
        
            