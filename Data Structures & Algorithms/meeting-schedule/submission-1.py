"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, -x.end))

        if len(intervals) == 0:
            return True

        curEnd = intervals[0].end
        for i in range(1, len(intervals)):
            cur = intervals[i]

            if cur.start < curEnd:
                return False
            
            curEnd = max(curEnd, cur.end)
        
        return True
