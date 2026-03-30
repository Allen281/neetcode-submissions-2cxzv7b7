import heapq

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        heap = []

        rslt = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while heap and heap[0][0] < temperatures[i]:
                rslt[heap[0][1]] = i - heap[0][1]
                heapq.heappop(heap)
            
            heapq.heappush(heap, (temperatures[i], i))
        
        return rslt