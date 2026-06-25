class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        edges = len(tickets)
        self.rslt = list()
        curPath = list()
        self.good = False

        for f, t in tickets:
            adj[f].append([t, False])
        
        for key in adj.keys():
            adj[key].sort()

        print(adj)

        def solve(cur: str, count: int) -> None:
            curPath.append(cur)

            if count == edges:
                self.rslt = curPath.copy()
                self.good = True
                return
            
            
            for i in range(len(adj[cur])):
                if self.good:
                    break
                dest, taken = adj[cur][i]
                if taken:
                    continue

                adj[cur][i][1] = True
                solve(dest, count+1)
                adj[cur][i][1] = False
            
            curPath.pop()

        solve("JFK", 0)
        return self.rslt
