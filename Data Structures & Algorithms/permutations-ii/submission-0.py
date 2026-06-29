class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        rslt = list()
        cur = list()
        visited = [False] * len(nums)

        def solve(counter: int) -> None:
            if counter == len(nums):
                rslt.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1] or visited[i]:
                    continue
                
                visited[i] = True
                cur.append(nums[i])

                solve(counter+1)

                cur.pop()
                visited[i] = False

        
        nums.sort()
        solve(0)
        return rslt