class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay = [float('inf')] * (n+1)
        adj = [[] for _ in range(n+1)]

        for t in times:
            adj[t[0]].append((t[1], t[2]))

        def solve(i: int, curDelay: int) -> None:
            if delay[i] > curDelay:
                delay[i] = curDelay
                for a, b in adj[i]:
                    solve(a, curDelay+b)
        
        solve(k, 0)

        rslt = 0
        for i in range(1, len(delay)):
            rslt = max(rslt, delay[i])
        
        return rslt if rslt != float('inf') else -1
            
