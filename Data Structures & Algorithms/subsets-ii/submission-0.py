class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rslt = list()
        used = [False] * len(nums)

        def solve(i):
            if i == len(nums):
                cur = list()
                for i in range(len(nums)):
                    if used[i]:
                        cur.append(nums[i])
                rslt.append(cur)
                return

            if i > 0 and not used[i-1] and nums[i-1] == nums[i]:
                solve(i+1)
            else:
                solve(i+1)
                used[i] = True
                solve(i+1)
                used[i] = False

            
        nums.sort()
        solve(0)
        return rslt