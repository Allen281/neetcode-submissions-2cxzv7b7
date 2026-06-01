class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rslt = []
        visited = [False] * len(nums)

        def solve(cur):
            if len(cur) == len(nums):
                rslt.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                cur.append(nums[i])
                solve(cur)
                cur.pop()
                visited[i] = False
        
        solve([])
        return rslt
