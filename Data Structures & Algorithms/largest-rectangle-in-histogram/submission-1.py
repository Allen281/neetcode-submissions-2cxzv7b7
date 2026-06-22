class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        bars = list()
        rslt = 0

        for i, h in enumerate(heights):
            min_index = i
            while bars and bars[-1][0] > h:
                rslt = max(rslt, bars[-1][0] * (i-bars[-1][1]))
                min_index = min(min_index, bars[-1][1])
                bars.pop()
            
            bars.append((h, min_index))
        
        while bars:
            rslt = max(rslt, bars[-1][0] * (len(heights)-bars[-1][1]))
            bars.pop()

        return rslt
                