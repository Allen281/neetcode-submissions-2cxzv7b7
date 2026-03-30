class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[2]] * len(position)

        for i in range(len(position)):
            pairs[i] = [position[i], speed[i]]
        
        pairs.sort(key=lambda x: -x[0])

        slowestTime = (target-pairs[0][0])/pairs[0][1]
        rslt = 1

        for i in range(1, len(pairs)):
            p = pairs[i]
            curTime = (target-p[0])/p[1]

            if curTime > slowestTime:
                rslt += 1
                slowestTime = curTime
        
        return rslt