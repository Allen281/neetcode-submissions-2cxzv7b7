class Solution:
    def hammingWeight(self, n: int) -> int:
        rslt = 0

        for i in range(32):
            rslt += 1 & n
            n >>= 1
        
        return rslt