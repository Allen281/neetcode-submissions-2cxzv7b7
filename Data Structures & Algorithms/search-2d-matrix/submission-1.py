class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m
        while l+1 < r:
            mid = (l+r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid
            else:
                r = mid
        
        l1, r1 = 0, n
        while l1 + 1 < r1:
            mid = (l1+r1) // 2
            if matrix[l][mid] == target:
                return True
            elif matrix[l][mid] < target:
                l1 = mid
            else:
                r1 = mid
        return matrix[l][l1] == target
        