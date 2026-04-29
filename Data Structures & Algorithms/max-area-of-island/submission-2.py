class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rslt = 0

        def findArea(x, y):
            # Base case: Out of bounds or we hit water (0)
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            
            # Mark the current land cell as visited by sinking it
            grid[x][y] = 0
            
            # The area is 1 (current cell) plus the area of all neighbors
            return (1 + 
                    findArea(x+1, y) + 
                    findArea(x-1, y) + 
                    findArea(x, y+1) + 
                    findArea(x, y-1))

        # Iterate through every cell in the grid
        for i in range(m):
            for j in range(n):
                # Only launch the DFS if we find an unvisited land cell
                if grid[i][j] == 1:
                    # Update max area with the result of the DFS
                    rslt = max(rslt, findArea(i, j))
        
        return rslt