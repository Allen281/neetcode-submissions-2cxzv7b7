class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = dict()

        def solve(p1: int, p2: int) -> int:
            if p1 == len(s1) and p2 == len(s2):
                return True
            if (p1, p2) in dp:
                return dp[(p1, p2)]
            
            i = p1 + p2
            canDo = False

            if p1 < len(s1) and s1[p1] == s3[i]:
                canDo |= solve(p1+1, p2)
            if p2 < len(s2) and s2[p2] == s3[i]:
                canDo |= solve(p1, p2+1)

            dp[(p1, p2)] = canDo
            return canDo
        
        return solve(0, 0)