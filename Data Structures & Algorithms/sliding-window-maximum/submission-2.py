import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        vals = []
        rslt = []

        l, r = 0, 0
        while r+1 < k:
            heapq.heappush(vals, (-nums[r], r))
            r += 1

        while r < len(nums):
            heapq.heappush(vals, (-nums[r], r))

            while vals and vals[0][1] < l:
                heapq.heappop(vals)
            
            rslt.append(-vals[0][0])

            l += 1
            r += 1

        return rslt      
