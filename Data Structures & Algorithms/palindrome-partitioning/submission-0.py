class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rslt = list()

        def isPalindrome(l: int, r: int) -> bool:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            
            return l >= r

        def solve(l: int, cur: list()) -> None:
            if l == len(s):
                rslt.append(cur.copy())
                return

            for r in range(l, len(s)):
                if isPalindrome(l, r):
                    cur.append(s[l:r+1])
                    solve(r+1, cur)
                    cur.pop()
        
        solve(0, [])
        return rslt