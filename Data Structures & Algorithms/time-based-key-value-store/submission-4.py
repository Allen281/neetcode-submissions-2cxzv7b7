class TimeMap:

    def __init__(self):
        self.hm = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = list()
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        left, right = 0, len(self.hm[key])
        while left+1 < right:
            mid = (left+right)//2
            pair = self.hm[key][mid]
            if pair[0] <= timestamp: left = mid
            else: right = mid
        
        return self.hm[key][left][1] if timestamp >= self.hm[key][left][0] else ""
