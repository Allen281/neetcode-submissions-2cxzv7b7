class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            cur = i
            amt = 0
            visited = set()
            while len(visited) < len(gas):
                amt += gas[cur] - cost[cur]
                if amt < 0:
                    break

                visited.add(cur)
                cur = (cur+1) % len(gas)
            
            if len(visited) == len(gas):
                return i

        return -1