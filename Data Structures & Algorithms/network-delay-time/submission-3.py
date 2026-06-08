class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        edges = [[] for _ in range(n+1)]

        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        rslt = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            rslt = w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))
        
        return rslt if len(visited) == n else -1
            
