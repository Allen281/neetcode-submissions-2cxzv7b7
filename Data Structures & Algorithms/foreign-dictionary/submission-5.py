class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        dep = {c: 0 for word in words for c in word}

        for i in range(len(words)-1):
            cur = words[i]
            next = words[i+1]

            if len(cur) > len(next) and cur[:len(next)] == next:
                return ""

            for j in range(len(cur)):
                if cur[j] != next[j]:
                    if next[j] not in adj[cur[j]]:
                        adj[cur[j]].add(next[j])
                        dep[next[j]] += 1
                    break

        q = deque()
        rslt = list()

        for k, v in dep.items():
            if v == 0:
                q.append(k)

        while q:
            cur = q.popleft()
            rslt.append(cur)

            for c in adj[cur]:
                dep[c] -= 1
                if dep[c] == 0:
                    q.append(c)

        if len(rslt) != len(dep):
            return ""
        
        return "".join(rslt)
        
        
        

