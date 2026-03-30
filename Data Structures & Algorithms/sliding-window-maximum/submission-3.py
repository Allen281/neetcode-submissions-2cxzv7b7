class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        vals = []
        rslt = []

        l, r = 0, 0
        while r+1 < k:
            while vals and nums[vals[-1]] < nums[r]:
                vals.pop()
            
            vals.append(r)
            r += 1
        
        while r < len(nums):
            while vals and nums[vals[-1]] < nums[r]:
                vals.pop()
            
            vals.append(r)

            while vals and vals[0] < l:
                vals.pop(0)

            rslt.append(nums[vals[0]])

            r += 1
            l += 1


        return rslt

