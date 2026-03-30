class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        rslt = 0
        curEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < curEnd:
                curEnd = min(intervals[i][1], curEnd)
                rslt += 1
            else:
                curEnd = intervals[i][1]
        
        return rslt