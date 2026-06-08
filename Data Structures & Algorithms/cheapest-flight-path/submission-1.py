class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        for f, t, p in flights:
            edges[f].append((t, p))
        
        minHeap = [(0, 0, src)]
        stopsTaken = dict()

        while minHeap:
            p1, d1, n1 = heapq.heappop(minHeap)

            if n1 == dst:
                return p1

            if d1 > k:
                continue

            if n1 in stopsTaken and stopsTaken[n1] <= d1:
                continue


            stopsTaken[n1] = d1

            for n2, p2 in edges[n1]:
                heapq.heappush(minHeap, (p2+p1, d1+1, n2))
        
        return -1