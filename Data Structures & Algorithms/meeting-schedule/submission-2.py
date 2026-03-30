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

        for i in range(0, len(intervals)-1):
            before, cur = intervals[i], intervals[i+1]

            if before.end > cur.start:
                return False
        
        return True
