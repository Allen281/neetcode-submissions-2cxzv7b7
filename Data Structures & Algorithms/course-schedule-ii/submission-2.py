class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        dependencies = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            dependencies[a] += 1

        q = deque()

        for i in range(len(dependencies)):
            if dependencies[i] == 0:
                q.append(i)
        
        rslt = list()
        while q:
            cur = q.popleft()
            rslt.append(cur)
            for a in adj[cur]:
                dependencies[a] -= 1
                if dependencies[a] == 0:
                    q.append(a)
        
        return rslt if len(rslt) == numCourses else []