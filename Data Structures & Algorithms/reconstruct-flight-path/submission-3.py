class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, to in sorted(tickets, reverse = True):
            adj[src].append(to)
        
        rslt = list()

        def solve(cur: str) -> None:
            while adj[cur]:
                solve(adj[cur].pop())
            
            rslt.append(cur)
        
        solve("JFK")
        return rslt[::-1]