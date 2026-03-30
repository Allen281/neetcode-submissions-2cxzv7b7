class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        rslt = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]

            if rslt[-1][1] >= cur[0]:
                rslt[-1][1] = max(cur[1], rslt[-1][1])
            else:
                rslt.append(cur)
        
        return rslt