class Solution:
    def countBits(self, n: int) -> List[int]:
        rslt = [0] * (n+1)

        for i in range(1, n+1):
            offset = pow(2,int(math.log2(i)))
            rslt[i] = 1 + rslt[i-offset]
        return rslt