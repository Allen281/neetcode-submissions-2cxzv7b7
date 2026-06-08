class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = float('inf')
        q = deque()
        max_time = [[-1 for _ in range(n)] for _ in range(m)]

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    max_time[x][y] = INF
                elif grid[x][y] == 2:
                    q.append((x, y, 0))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            cur = q.popleft()
            x, y, l = cur[0], cur[1], cur[2]

            for dx, dy in directions:
                nx, ny = x+dx, y+dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == 0:
                    continue
                
                if max_time[nx][ny] == INF:
                    max_time[nx][ny] = l+1
                    q.append((nx, ny, l+1))

        rslt = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    if max_time[x][y] == INF:
                        return -1
                    else:
                        rslt = max(rslt, max_time[x][y])
        return rslt
            
            