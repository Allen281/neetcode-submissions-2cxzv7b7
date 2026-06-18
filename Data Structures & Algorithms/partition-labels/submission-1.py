class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = dict()

        for i, c in enumerate(s):
            lastIndex[c] = i
        
        rslt = list()
        size = 0
        cur_last = 0

        for i, c in enumerate(s):
            size += 1

            cur_last = max(cur_last, lastIndex[c])

            if i == cur_last:
                rslt.append(size)
                size = 0
        
        return rslt
            