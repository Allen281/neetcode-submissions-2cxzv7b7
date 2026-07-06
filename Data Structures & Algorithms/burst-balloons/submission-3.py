class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = dict()
        n = len(nums)
        
        for i in range(1, n-1):
            for l in range(1, n-i):
                r = l + i -1

                rslt = 0
                for j in range(l, r+1):
                    cur_val = nums[j] * nums[l-1] * nums[r+1] + dp.get((l, j-1), 0) + dp.get((j+1, r), 0)
                    rslt = max(rslt, cur_val)
                dp[(l, r)] = rslt
        
        return dp[(1, n-2)]
