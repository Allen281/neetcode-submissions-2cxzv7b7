class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rslt = []

        def solve(i, cur):
            if i == len(nums):
                return rslt.append(cur.copy())
            
            solve(i+1, cur)
            cur.append(nums[i])
            solve(i+1, cur)
            
            cur.pop()
        
        solve(0, [])
        return rslt