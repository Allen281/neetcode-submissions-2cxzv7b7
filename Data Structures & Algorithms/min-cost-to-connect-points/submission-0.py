class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(a: int, b: int) -> float:
            return abs(points[a][0]-points[b][0]) + abs(points[a][1]-points[b][1])

        minHeap = []
        visited = set()
        edges = [[] for _ in range(len(points))]

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = distance(i, j)
                edges[i].append((j, dist))
                edges[j].append((i, dist))

        rslt = 0
        minHeap.append((0, 0))

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            rslt += w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2, n2))

        return rslt