class Solution:
    class Region:
        def __init__(self):
            self.points: list() = []
            self.isTrapped: bool = True

    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def traverseRegion(x: int, y: int, r: Region) -> None:
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == 'X' or (x, y) in visited:
                return
            
            visited.add((x, y))
            r.points.append((x, y))

            if x == 0 or x == len(board)-1 or y == 0 or y == len(board[0])-1:
                r.isTrapped = False

            traverseRegion(x+1, y, r)
            traverseRegion(x-1, y, r)
            traverseRegion(x, y+1, r)
            traverseRegion(x, y-1, r)

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 'O' and (x, y) not in visited:
                    region = self.Region()
                    traverseRegion(x, y, region)
                    if region.isTrapped:
                        for a, b in region.points:
                            board[a][b] = 'X'