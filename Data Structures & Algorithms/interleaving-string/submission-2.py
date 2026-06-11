class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False

        dp = dict()

        def solve(i: int, turn: int, p1: int, p2: int):
            if i == len(s3):
                return p1 == len(s1) and p2 == len(s2)
            if (i, turn) in dp:
                return dp[(i, turn)]
            
            canDo = False
            if turn == 1:
                p1_counter = p1
                while p1_counter < len(s1) and s3[i] == s1[p1_counter]:
                    p1_counter += 1
                    canDo |= solve(i+1, 1, p1_counter, p2)
                
                if p2 < len(s2) and s3[i] == s2[p2]:
                    canDo |= solve(i+1, 2, p1, p2+1)
            else:
                p2_counter = p2
                while p2_counter < len(s2) and s3[i] == s2[p2_counter]:
                    p2_counter += 1
                    canDo |= solve(i+1, 2, p1, p2_counter)
                
                if p1 < len(s1) and s3[i] == s1[p1]:
                    canDo |= solve(i+1, 1, p1+1, p2)
            
            dp[(i, turn)] = canDo
            return canDo
        
        return solve(0, 1, 0, 0) or solve(0, 2, 0, 0)
