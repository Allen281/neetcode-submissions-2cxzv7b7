class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        
        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            a, b = 0, 0
            while a < len(first) and b < len(second):
                if first[a] != second[b]:
                    adj[first[a]].add(second[b])
                    break
                a += 1
                b += 1
            
            if b == len(second) and a < len(first):
                return ''
        
        visited = {}
        rslt = []

        def generateOrder(c):
            if c in visited:
                return visited[c]

            visited[c] = False
            
            for i in adj[c]:
                if not generateOrder(i):
                    return False
            
            rslt.append(c)
            visited[c] = True
            return True

        for c in adj:
            if not generateOrder(c):
                return ''

        rslt.reverse()
        return "".join(rslt)
