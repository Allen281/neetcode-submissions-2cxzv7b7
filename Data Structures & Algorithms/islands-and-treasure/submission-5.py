from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Edge case: empty grid
        if not grid or not grid[0]:
            return

        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        # 1. Find all treasures and add them to the queue first
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # Append row, column, and current distance (0)
                    q.append((r, c, 0))

        # Directions for moving: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. Expand outward from all treasures simultaneously
        while q:
            r, c, dist = q.popleft()

            # Check all 4 surrounding cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Step A: Skip if out of bounds
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                
                # Step B: Only process completely unvisited empty rooms
                if grid[nr][nc] == INF:
                    # Claim the room immediately so no other path overwrites it
                    grid[nr][nc] = dist + 1
                    
                    # Add it to the queue to explore its neighbors later
                    q.append((nr, nc, dist + 1))