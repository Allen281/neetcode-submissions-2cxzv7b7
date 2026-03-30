class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canDo(k):
            time = 0

            for p in piles:
                time += math.ceil(p/k)
            
            return time <= h
        
        left, right = 0, 1e9

        while left+1 < right:
            mid = (left+right)//2
            if canDo(mid):
                right = mid
            else:
                left = mid

        return (int)(right)