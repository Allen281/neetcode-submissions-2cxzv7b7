class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False] * 3

        for t in triplets:
            if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                good[0] = True
            if t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2]:
                good[1] = True
            if t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2]:
                good[2] = True

        return good[0] and good[1] and good[2]
            