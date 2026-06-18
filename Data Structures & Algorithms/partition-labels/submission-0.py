class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_last = dict()

        for i, c in enumerate(s):
            if c in first_last:
                first_last[c][1] = i
            else:
                first_last[c] = [i, i]

        ranges = list()
        for v in first_last.values():
            ranges.append(v)
        
        ranges.sort()
        rslt = list()
        cur_range = [0, 0]

        for f, l in ranges:
            print(f'Cur: {f}, {l}')
            if f <= cur_range[1]:
                cur_range[1] = max(l, cur_range[1])
            else:
                print(cur_range)
                rslt.append(cur_range[1]-cur_range[0]+1)
                cur_range = [f, l]
        
        rslt.append(cur_range[1]-cur_range[0]+1)
        

        return rslt
        
