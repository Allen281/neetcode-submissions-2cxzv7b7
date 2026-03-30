class Solution:
    def longestPalindrome(self, s: str) -> str:

        def solve(s, l, r):
            if l < 0 or r >= len(s):
                return l+1, r-1
            
            if s[l] == s[r]:
                return solve(s, l-1, r+1)
            else:
                return l+1, r-1
        
        left, right = 0, 0

        for i in range(len(s)):
            tL, tR = solve(s, i, i)
            if tR-tL > right-left:
                left = tL
                right = tR
        
        for i in range(len(s)-1):
            tL, tR = solve(s, i, i+1);
            if tR-tL > right-left:
                left = tL
                right = tR

        return s[left:right+1]
