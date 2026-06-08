class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(n: int) -> int:
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(a: int, b: int) -> bool:
            r1, r2 = find(a), find(b)

            if r1 == r2:
                return False
            else:
                parent[r2] = r1
                return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]