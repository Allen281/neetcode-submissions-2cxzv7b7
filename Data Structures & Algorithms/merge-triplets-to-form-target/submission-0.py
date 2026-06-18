class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count_good = 0

        for i in range(3):
            for t in triplets:
                if t[i] == target[i]:
                    if t[i-1] <= target[i-1] and t[i-2] <= target[i-2]:
                        count_good += 1
                        break
        
        return count_good == 3