class Solution:
    def countSubstrings(self, s: str) -> int:

        def solve(s, l, r, counter):
            if l < 0 or r >= len(s):
                return counter
            
            if s[l] == s[r]:
                return solve(s, l-1, r+1, counter+1)
            else:
                return counter
        
        counter = 0
        for i in range(len(s)):
            counter += solve(s, i, i, 0)
        
        for i in range(len(s)-1):
            counter += solve(s, i, i+1, 0)

        return counter