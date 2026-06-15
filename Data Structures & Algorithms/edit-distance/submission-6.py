class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = dict()
        dp[(len(word1), len(word2))] = 0

        def solve(p1: int, p2: int) -> int:
            if p2 == len(word2) and p1 != len(word1):
                return len(word1)-p1

            if (p1, p2) in dp:
                return dp[(p1, p2)]

            if p1 == len(word1):
                return len(word2)-p2

            if word1[p1] == word2[p2]:
                dp[(p1, p2)] = solve(p1+1, p2+1)
            else:
                replace = solve(p1+1, p2+1)
                erase = solve(p1, p2+1)
                insert = solve(p1+1, p2)
                dp[(p1, p2)] = min(replace, erase, insert) + 1
            
            return dp[(p1, p2)]
        
        return solve(0, 0)