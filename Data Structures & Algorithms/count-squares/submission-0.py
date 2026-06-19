class CountSquares:

    def __init__(self):
        self.coords = dict()

    def add(self, point: List[int]) -> None:
        self.coords[(point[0], point[1])] = self.coords.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        rslt = 0
        for c, v in self.coords.items():
            if c[0] == point[0] or c[1] == point[1]:
                continue
            
            if abs(c[0]-point[0]) != abs(c[1]-point[1]):
                continue

            corner1 = self.coords.get((c[0], point[1]), 0)
            corner2 = self.coords.get((point[0], c[1]), 0)

            rslt += v * corner1 * corner2
        
        return rslt
