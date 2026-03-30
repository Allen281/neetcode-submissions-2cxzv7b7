class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        mid = int(n/2)

        for i in range(mid):
            temp = matrix[i]
            matrix[i] = matrix[n-i-1]
            matrix[n-i-1] = temp
        
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        