import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = dict()
        for t in tasks:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1

        pq = []
        for value in freq.values():
            pq.append(-value)
        
        heapq.heapify(pq)
        q = deque()

        time = 0
        while pq or q:
            while q:
                task = q[0]
                if task[1] > time:
                    break
                heapq.heappush(pq, task[0])
                q.popleft()
            
            if not pq and q:
                time = q[0][1]
            
            else:
                task = heapq.heappop(pq)
                task += 1
                time += 1
                if task != 0:
                    q.append((task, time+n))
        
        return time


