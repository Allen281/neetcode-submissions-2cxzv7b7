import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        insertedVals = []
        removedVals = []
        rslt = []

        l, r = 0, 0
        while r+1 < k:
            heapq.heappush(insertedVals, -nums[r])
            r += 1

        while r < len(nums):
            heapq.heappush(insertedVals, -nums[r])

            rslt.append(-insertedVals[0])

            heapq.heappush(removedVals, -nums[l])
            l += 1
            r += 1

            while removedVals and insertedVals and removedVals[0] == insertedVals[0]:
                heapq.heappop(removedVals) 
                heapq.heappop(insertedVals)

        return rslt      
