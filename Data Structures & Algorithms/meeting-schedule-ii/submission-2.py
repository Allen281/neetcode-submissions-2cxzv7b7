"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key=lambda x:(x.start, x.end))

        for x in intervals:
            if rooms and rooms[0] <= x.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, x.end)
        
        return len(rooms)